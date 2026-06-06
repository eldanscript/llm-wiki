#!/usr/bin/env python3
"""
wiki_ingest.py — 변경된 Raw 노트(0-5 폴더)를 감지해 Claude API로 6.Wiki/ 페이지를 자동 생성·업데이트.

Usage:
    python scripts/wiki_ingest.py            # CI: git diff HEAD~1 기반
    python scripts/wiki_ingest.py --folder 2.Areas/NVidia  # 특정 폴더 강제 처리
"""

import os
import sys
import json
import subprocess
import re
import argparse
from pathlib import Path
from datetime import date

import anthropic

VAULT_ROOT = Path(__file__).parent.parent
WIKI_DIR = VAULT_ROOT / "6.Wiki"
RAW_PREFIXES = ("0.Slip-box", "1.Projects", "2.Areas", "3.Resources", "4.Archive", "5.Periodic Notes")
MODEL = "claude-haiku-4-5"
MAX_FILE_CHARS = 15000
MAX_EXISTING_WIKI_CHARS = 8000


# ---------------------------------------------------------------------------
# 변경 파일 감지
# ---------------------------------------------------------------------------

def get_changed_files() -> list[str]:
    """git diff HEAD~1 에서 0-5 폴더의 .md 파일 목록 반환."""
    result = subprocess.run(
        ["git", "diff", "HEAD~1", "--name-only", "--diff-filter=ACMR"],
        capture_output=True, text=True, cwd=VAULT_ROOT
    )
    files = []
    for line in result.stdout.strip().splitlines():
        if any(line.startswith(p) for p in RAW_PREFIXES) and line.endswith(".md"):
            files.append(line)
    return files


def group_by_area(files: list[str]) -> dict[str, list[str]]:
    """
    파일을 '상위폴더/두번째폴더' 단위로 그룹핑.
    예) 2.Areas/NVidia/Session/file.md  →  key = "2.Areas/NVidia"
        1.Projects/Raingent/x.md        →  key = "1.Projects/Raingent"
    """
    groups: dict[str, list[str]] = {}
    for f in files:
        parts = Path(f).parts
        key = str(Path(parts[0]) / parts[1]) if len(parts) > 2 else parts[0]
        groups.setdefault(key, []).append(f)
    return groups


# ---------------------------------------------------------------------------
# Wiki 파일 읽기
# ---------------------------------------------------------------------------

def read_text(path: Path, max_chars: int = 0) -> str:
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8", errors="ignore")
    if max_chars and len(text) > max_chars:
        text = text[:max_chars] + "\n\n[... 이하 생략 ...]"
    return text


def read_existing_wiki_pages() -> dict[str, str]:
    pages = {}
    for p in WIKI_DIR.rglob("*.md"):
        rel = str(p.relative_to(WIKI_DIR))
        if rel not in ("WIKI_SCHEMA.md", "log.md", "LLM-Wiki-Guide.md"):
            pages[rel] = p.read_text(encoding="utf-8", errors="ignore")
    return pages


# ---------------------------------------------------------------------------
# Claude API 호출
# ---------------------------------------------------------------------------

def call_claude_ingest(
    folder: str,
    files: list[str],
    wiki_schema: str,
    wiki_index: str,
    existing_pages: dict[str, str],
) -> dict:
    today = date.today().isoformat()

    # 소스 파일 내용 조합
    file_blocks = []
    for f in files:
        content = read_text(VAULT_ROOT / f, MAX_FILE_CHARS)
        if content:
            file_blocks.append(f"=== {f} ===\n{content}")
    files_text = "\n\n".join(file_blocks) if file_blocks else "(변경된 파일 없음)"

    # 관련 기존 Wiki 페이지 선별 (폴더명 키워드 매칭 + index)
    folder_keywords = Path(folder).name.lower().split("-")
    relevant: dict[str, str] = {"index.md": wiki_index}
    for k, v in existing_pages.items():
        if any(kw in k.lower() for kw in folder_keywords):
            relevant[k] = v[:MAX_EXISTING_WIKI_CHARS]
    existing_text = "\n\n".join(
        f"=== 6.Wiki/{k} ===\n{v}" for k, v in relevant.items()
    )

    prompt = f"""You manage a `6.Wiki/` directory following the WIKI_SCHEMA rules below.
Today is {today}.

## WIKI_SCHEMA
{wiki_schema}

## CHANGED SOURCE FILES  (under `{folder}`)
{files_text}

## RELEVANT EXISTING WIKI PAGES
{existing_text}

## Task
Based on the changed source files, generate or update the appropriate `6.Wiki/` pages.
- Follow WIKI_SCHEMA frontmatter and structure exactly.
- Preserve existing Wiki content — extend, do not overwrite unrelated sections.
- For a new area/folder with no existing mapping, create the most appropriate pages
  (entity page, topic page, or both) and add to WIKI_SCHEMA mapping.
- All text in Korean unless technical terms.

Respond with ONLY valid JSON — no markdown fences, no extra commentary:
{{
  "changes": [
    {{
      "wiki_path": "Entities/Companies/NVidia.md",
      "action": "create",
      "content": "...full markdown..."
    }}
  ],
  "index_entries": [
    {{
      "section": "Companies",
      "line": "- [[Entities/Companies/NVidia]] — one-line description"
    }}
  ],
  "schema_mapping": "| `{folder}/` | `Entities/Companies/NVidia.md`, `Topics/GTC-Taipei-2026.md` |",
  "log_entry": "[{today}] INGEST: {folder} → <generated pages>"
}}"""

    client = anthropic.Anthropic()
    response = client.messages.create(
        model=MODEL,
        max_tokens=8096,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = response.content[0].text.strip()
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)
    return json.loads(raw)


# ---------------------------------------------------------------------------
# 결과 적용
# ---------------------------------------------------------------------------

def apply_changes(result: dict, today: str):
    """Wiki 페이지 쓰기, index/schema/log 업데이트."""

    # 1. Wiki 페이지 생성·업데이트
    for change in result.get("changes", []):
        rel_path = change["wiki_path"]
        if rel_path.startswith("6.Wiki/"):
            rel_path = rel_path[len("6.Wiki/"):]
        wiki_path = WIKI_DIR / rel_path
        wiki_path.parent.mkdir(parents=True, exist_ok=True)
        wiki_path.write_text(change["content"], encoding="utf-8")
        action = "Created" if change["action"] == "create" else "Updated"
        print(f"  [{action}] {rel_path}")

    # 2. index.md 업데이트
    index_path = WIKI_DIR / "index.md"
    index_content = read_text(index_path)
    changed_index = False
    for entry in result.get("index_entries", []):
        section = entry["section"]
        line = entry["line"].strip()
        if line and line not in index_content:
            pattern = f"### {section}\n"
            if pattern in index_content:
                index_content = index_content.replace(pattern, f"{pattern}{line}\n", 1)
            else:
                index_content += f"\n### {section}\n{line}\n"
            changed_index = True
    if changed_index:
        # 갱신 날짜 업데이트
        index_content = re.sub(
            r"마지막 갱신: \d{4}-\d{2}-\d{2}",
            f"마지막 갱신: {today}",
            index_content,
        )
        index_path.write_text(index_content, encoding="utf-8")
        print("  [Updated] index.md")

    # 3. WIKI_SCHEMA.md 매핑 추가
    schema_line = (result.get("schema_mapping") or "").strip()
    if schema_line:
        schema_path = WIKI_DIR / "WIKI_SCHEMA.md"
        schema_content = read_text(schema_path)
        if schema_line not in schema_content:
            # "## 5. Vault → Wiki 매핑" 섹션의 마지막 행 뒤에 삽입
            schema_content = re.sub(
                r"(\| `4\.Archive.*?\|[^\n]*\n)",
                r"\1" + schema_line + "\n",
                schema_content,
                count=1,
            )
            # 위 패턴이 없으면 테이블 끝에 붙이기
            if schema_line not in schema_content:
                schema_content += f"\n{schema_line}\n"
            schema_path.write_text(schema_content, encoding="utf-8")
            print("  [Updated] WIKI_SCHEMA.md")

    # 4. log.md append (최신 항목이 상단)
    log_entry = (result.get("log_entry") or "").strip()
    if log_entry:
        log_path = WIKI_DIR / "log.md"
        log_content = read_text(log_path)
        separator = "---\n\n"
        if separator in log_content:
            log_content = log_content.replace(separator, f"{separator}{log_entry}\n\n", 1)
        else:
            log_content = f"{log_entry}\n\n{log_content}"
        log_path.write_text(log_content, encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", help="특정 폴더 강제 처리 (예: 2.Areas/NVidia)")
    args = parser.parse_args()

    today = date.today().isoformat()

    if args.folder:
        # 폴더 내 모든 .md 파일 수집
        target = VAULT_ROOT / args.folder
        files = [str(p.relative_to(VAULT_ROOT)) for p in target.rglob("*.md")]
        groups = {args.folder: files}
    else:
        files = get_changed_files()
        if not files:
            print("0-5 폴더에 변경된 파일 없음. 종료.")
            sys.exit(0)
        groups = group_by_area(files)

    print(f"처리 대상 그룹: {list(groups.keys())}")

    wiki_schema = read_text(WIKI_DIR / "WIKI_SCHEMA.md")
    wiki_index = read_text(WIKI_DIR / "index.md")
    existing_pages = read_existing_wiki_pages()

    MAX_FILES_PER_CALL = 5
    for folder, folder_files in groups.items():
        batches = [folder_files[i:i+MAX_FILES_PER_CALL] for i in range(0, len(folder_files), MAX_FILES_PER_CALL)]
        for idx, batch in enumerate(batches, 1):
            print(f"\n--- Ingesting: {folder} ({len(batch)}개 파일, batch {idx}/{len(batches)}) ---")
            result = call_claude_ingest(folder, batch, wiki_schema, wiki_index, existing_pages)
            apply_changes(result, today)
            existing_pages = read_existing_wiki_pages()
            wiki_index = read_text(WIKI_DIR / "index.md")

    print("\n완료.")


if __name__ == "__main__":
    main()
