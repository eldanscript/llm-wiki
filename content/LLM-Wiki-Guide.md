# Obsidian LLM Wiki 구축 가이드

> Karpathy의 LLM Wiki 패턴을 Obsidian Vault에 적용한 구현 가이드  
> 최초 작성: 2026-05-31 | 최종 업데이트: 2026-05-31  
> 참조: [Karpathy LLM Wiki Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

---

## 1. LLM Wiki 패턴이란?

Andrej Karpathy가 제안한 **AI가 직접 유지·관리하는 지식 베이스** 아키텍처.  
기존 RAG(검색 증강 생성)와 달리, LLM이 원본 문서를 미리 읽고 **합성된 Wiki 페이지**를 생성해 누적 저장한다.

> "The wiki is a persistent, compounding artifact that evolves as sources are added and questions are asked."  
> — Andrej Karpathy

### 핵심 차별점

| 방식 | 동작 | 특징 |
|------|------|------|
| RAG | 질의 시마다 원본 문서 검색·전달 | 느림, 원본 노이즈 포함 |
| **LLM Wiki** | 미리 합성된 Wiki 페이지 참조 | 빠름, 정제된 지식, 누적 성장 |

---

## 2. 3-Layer 아키텍처

```
┌──────────────────────────────────────────┐
│  Layer 3: Schema (WIKI_SCHEMA.md)        │  ← 구조 규칙 정의
├──────────────────────────────────────────┤
│  Layer 2: Wiki (6.Wiki/)                 │  ← LLM이 생성·관리
│    Concepts / Entities / Projects /      │
│    Topics / Tools / index.md / log.md    │
├──────────────────────────────────────────┤
│  Layer 1: Raw Sources (불변)             │  ← 원본 노트 (절대 수정 금지)
│    0.Slip-box / 1.Projects / 2.Areas /   │
│    3.Resources / 4.Archive               │
└──────────────────────────────────────────┘
```

**핵심 원칙**: Raw Sources는 LLM이 읽기만 하고 절대 수정하지 않는다.  
Wiki 페이지만 LLM이 생성·업데이트한다.

---

## 3. 구축된 Wiki 구조

### 폴더 구조

```
6.Wiki/
├── WIKI_SCHEMA.md          # 운영 규칙 (Schema)
├── index.md                # 전체 카탈로그
├── log.md                  # 작업 이력 (append-only)
├── LLM-Wiki-Guide.md       # 이 문서
├── LLM-Wiki-Guide.pdf      # PDF 버전
├── Concepts/               # 추상 개념
│   ├── Agentic-AI.md
│   ├── Interpretability.md
│   ├── LLM-Wiki-Pattern.md
│   └── Multi-Agent-System.md
├── Entities/
│   └── Companies/          # 기업 엔티티
│       ├── Anthropic.md
│       └── FuriosaAI.md
├── Projects/               # 프로젝트 요약
│   └── Raingent.md
├── Tools/                  # 도구·소프트웨어
│   ├── Claude-Code.md
│   ├── Finance-Agent.md
│   ├── GSD.md
│   ├── Obsidian.md
│   ├── QMD.md
│   ├── RTK.md
│   ├── TMUX.md
│   ├── Tailscale.md
│   ├── Tech-Report-Agent.md
│   └── gstack.md
└── Topics/                 # 주제별 합성 페이지
    ├── AWS-Summit-Seoul-2026.md
    └── NPU-AI-Chip-Landscape.md
```

### Wiki 페이지 형식

모든 Wiki 페이지는 아래 frontmatter를 포함한다:

```yaml
---
wiki_type: concept | entity | project | topic
tags: [wiki, <category>]
sources:
  - "원본 파일 경로 또는 [[링크]]"
updated: YYYY-MM-DD
---
```

---

## 4. 3가지 핵심 운영 동작

### 4-1. Ingest (새 소스 반영)

새로운 노트나 아티클을 Wiki에 통합하는 과정.  
**수동 요청** 또는 **Git Hook 자동 실행**(→ 5장 참조) 두 가지 방식을 지원한다.

**수동 요청 예시:**
```
3.Resources/Tech Report/Anthropic Blog/Articles/2026-04-02_LLM의 감정 개념.md
위 파일을 읽고 Wiki에 인제스트해줘.
관련 Concept 페이지가 없으면 새로 생성하고,
Anthropic.md도 업데이트해줘.
```

**Claude의 판단 원칙:**
- 관련 Wiki 페이지가 이미 있으면 → 해당 페이지에 섹션 추가 (통합)
- 완전히 새로운 개념·엔티티면 → 새 페이지 생성
- 항상 `index.md`와 `log.md`를 마지막에 업데이트

---

### 4-2. Query (Wiki로 질문 답변)

Wiki 페이지만 참조해 질문에 즉시 답변한다. Raw source를 다시 읽지 않아도 된다.

**예시:**
```
Wiki를 참조해서 답해줘:
"Raingent 프로젝트에서 Finance Agent가 하는 일과 현재 상태는?"
```

답변 후 유용한 Q&A는 Topics 페이지로 저장할 수 있다:
```
이 답변을 6.Wiki/Topics/Finance-Agent-FAQ.md 로 저장해줘.
```

---

### 4-3. Lint (품질 점검)

주기적으로 Wiki 상태를 점검해 품질을 유지한다.

| 항목 | 설명 |
|------|------|
| 고아 페이지 | `index.md`에 등록되지 않은 페이지 |
| sources 누락 | frontmatter에 `sources:` 필드가 없는 페이지 |
| 깨진 링크 | 존재하지 않는 파일을 참조하는 `[[링크]]` |
| 오래된 페이지 | `updated` 날짜가 6개월 이상 된 페이지 |
| 중복 개념 | 동일 개념을 다루는 페이지가 2개 이상 |

```
6.Wiki 전체에 대해 Lint를 실행해줘.
고아 페이지, sources 누락, 깨진 링크를 확인하고 결과를 log.md에 기록해줘.
```

---

## 5. 자동 인제스트 시스템 (Git Hook)

Obsidian에 노트를 저장하면 **사람 개입 없이** Wiki가 자동 업데이트된다.

### 5-1. 동작 흐름

```
Obsidian에서 노트 저장
       │
       ▼ (obsidian-git 플러그인, 10분 주기)
git commit 자동 실행
       │
       ▼ post-commit hook 발동
wiki-ingest.sh 백그라운드 실행
       │
       ├─ 새 .md 파일 없음 → SKIP 기록 후 종료
       │
       └─ 새 .md 파일 감지
              │
              ▼ claude --print (비대화형)
         파일 읽기 → Wiki 페이지 생성/수정
              │
              ▼
         log.md, index.md 업데이트 → 완료
```

### 5-2. 구성 파일

| 파일 | 역할 |
|------|------|
| `.git/hooks/post-commit` | git 커밋 직후 자동 실행되는 훅 |
| `~/scripts/wiki-ingest.sh` | 새 파일 감지 및 Claude 호출 스크립트 |
| `~/scripts/wiki-ingest.log` | 자동 인제스트 실행 이력 |

**post-commit 훅** (`.git/hooks/post-commit`):
```bash
#!/bin/bash
INGEST_SCRIPT="/home/rainny/scripts/wiki-ingest.sh"
if [ -x "$INGEST_SCRIPT" ]; then
  nohup bash "$INGEST_SCRIPT" >> /home/rainny/scripts/wiki-ingest.log 2>&1 &
fi
exit 0
```

**인제스트 스크립트** (`~/scripts/wiki-ingest.sh`):
```bash
#!/bin/bash
VAULT="/home/rainny/문서/Obsidian Vault"
cd "$VAULT" || exit 1

# 한글 파일명 정상 처리를 위해 core.quotepath=false 필수
NEW_FILES=$(git -c core.quotepath=false diff HEAD~1 \
  --name-only --diff-filter=A \
  | grep '\.md$' | grep -v '^6\.Wiki/' | grep -v '^\.') 

[ -z "$NEW_FILES" ] && exit 0

claude --print "다음 파일들을 읽고 WIKI_SCHEMA 규칙에 따라
6.Wiki를 업데이트해줘: $NEW_FILES"
```

> **주의**: 한글·공백이 포함된 파일명은 git이 octal 인코딩(`\352\263\265...`)으로 출력한다.  
> `core.quotepath=false` 없이는 `.md` 패턴 매칭이 실패한다.

### 5-3. 자동 권한 설정

`claude --print`가 권한 프롬프트 없이 실행되려면 Vault의 `.claude/settings.json`에 아래 허용 목록이 필요하다:

```json
{
  "permissions": {
    "allow": [
      "Read(**)",
      "Write(**)",
      "Edit(**)",
      "MultiEdit(**)",
      "Bash(find *)",
      "Bash(ls *)",
      "Bash(ls)",
      "Bash(mkdir *)",
      "Bash(cat *)",
      "mcp__obsidian__vault_write",
      "mcp__obsidian__vault_append",
      "mcp__obsidian__vault_patch",
      "mcp__obsidian__vault_read",
      "mcp__obsidian__vault_list",
      "mcp__obsidian__vault_delete",
      "mcp__obsidian__vault_move",
      "mcp__obsidian__search_simple",
      "mcp__obsidian__search_query"
    ]
  }
}
```

> `Write(**)`는 신규 파일 생성만 커버한다.  
> 기존 파일 수정(`index.md`, `log.md` 업데이트)에는 `Edit(**)`가 별도로 필요하다.

### 5-4. 실제 동작 확인 결과

`2.Areas/AgenticAI/claude_hooks_guide.md` 커밋 후 자동 인제스트 결과:

```
[2026-05-31 22:29:10] INGEST 시작: 2.Areas/AgenticAI/claude_hooks_guide.md
[2026-05-31 22:29:10] INGEST 완료 (exit 0)
→ Tools/Claude-Code.md — Hooks 이벤트 섹션 신규 삽입
→ log.md, index.md 자동 업데이트
```

- 커밋 후 즉시 실행, 사람 개입 없음
- Claude가 기존 `Claude-Code.md`에 통합 (WIKI_SCHEMA 규칙 자동 준수)

---

## 6. 일상적인 사용 워크플로우

```
Obsidian에서 노트 저장
       │
       ▼ (obsidian-git, 10분 이내 자동 커밋)
       │
       ▼ (post-commit hook → wiki-ingest.sh)
Wiki 자동 업데이트 ◀────────────────────────────┐
       │                                        │
       ├── 궁금한 것 → Claude: "Wiki에서 ~~알려줘"   │
       │              즉시 답변                  │
       │                                        │
       ├── 주간 → Claude: "Wiki Lint 실행해줘"    │
       │         품질 유지                       │
       │                                        │
       └── 새 노트 저장 ──────────────────────────┘
```

**수동 인제스트가 필요한 경우:**
- 기존 파일을 대폭 수정했을 때 (수정은 `--diff-filter=A`로 감지 안 됨)
- 즉시 반영이 필요할 때 (10분 커밋 주기 기다리지 않을 때)

```
이 파일을 지금 바로 Wiki에 인제스트해줘: <파일 경로>
```

---

## 7. 4-Agent 병렬 초기 구축 방법

처음 대용량 Vault를 구축할 때, tmux 4-pane 환경에서 agent를 병렬 실행한다.

| Agent | Pane | 담당 영역 | 생성 위치 |
|-------|------|-----------|-----------|
| Agent 0 | Pane 0 | `1.Projects/` | `Wiki/Projects/`, `Wiki/Tools/` |
| Agent 1 | Pane 1 | `2.Areas/AgenticAI`, `KnowledgeBase/` | `Wiki/Concepts/` |
| Agent 2 | Pane 2 | `3.Resources/Tech Report/` | `Wiki/Entities/Companies/` |
| Agent 3 | Pane 3 | `2.Areas/AWS`, `FuriosaAI/` + index 완성 | `Wiki/Topics/`, `Wiki/index.md` |

tmux pane에 프롬프트 전송:
```bash
tmux load-buffer /tmp/agent0_prompt.txt
tmux paste-buffer -t raingent:0.0
tmux send-keys -t raingent:0.0 "" Enter
```

---

## 8. 현재 구축 현황 (2026-05-31)

### 생성된 Wiki 페이지: 23개

**Concepts (4)**
- `Agentic-AI.md` — LLM 자율 실행 패러다임
- `Interpretability.md` — Mechanistic Interpretability, 감정 벡터
- `LLM-Wiki-Pattern.md` — Karpathy의 Wiki 아키텍처
- `Multi-Agent-System.md` — Orchestrator/Subagent 패턴

**Entities (2)**
- `Anthropic.md` — Claude 모델 계보, 335건 아티클 기반
- `FuriosaAI.md` — RNGD NPU, TCP 아키텍처

**Projects (1)**
- `Raingent.md` — Ubuntu PC AI 에이전트 생태계 전체 요약

**Tools (11)**
- `Claude-Code.md` — Hooks 이벤트 섹션 포함 (자동 인제스트로 업데이트됨)
- Finance-Agent, GSD, Obsidian, QMD, RTK, TMUX, Tailscale, Tech-Report-Agent, gstack

**Topics (2)**
- `AWS-Summit-Seoul-2026.md`, `NPU-AI-Chip-Landscape.md`

### Lint 상태 (2026-05-31 기준)
- 고아 페이지: **0건**
- sources 누락: **0건**
- 모든 updated 날짜: **2026-05-31** 최신

### 자동 인제스트 시스템
- **상태**: ✅ 운영 중
- **처리 방식**: obsidian-git 자동 커밋 → post-commit hook → `claude --print`
- **검증**: `claude_hooks_guide.md` 커밋 후 `Claude-Code.md` 자동 업데이트 확인

---

## 9. 향후 확장 방향

| 항목 | 상태 | 내용 |
|------|------|------|
| 자동 Ingest | ✅ 완료 | Git Hook + claude --print, 10분 이내 자동 반영 |
| **수정 파일 감지** | 예정 | `--diff-filter=M` 으로 대폭 수정된 파일도 재인제스트 |
| **Entities/Models** | 예정 | Claude, GPT, Gemini 등 모델 페이지 추가 |
| **Entities/People** | 예정 | Karpathy, Dario Amodei 등 주요 인물 페이지 |
| **Topics/Monthly** | 예정 | 월간 AI 트렌드 합성 페이지 자동 생성 |
| **Query 로그** | 예정 | 자주 묻는 질문을 Topics로 자동 전환 |
| **Obsidian Graph** | 예정 | `6.Wiki/` 폴더만 필터링한 지식 그래프 뷰 설정 |

---

## 10. 관련 파일

| 파일 | 경로 |
|------|------|
| Wiki Schema | `6.Wiki/WIKI_SCHEMA.md` |
| Wiki Index | `6.Wiki/index.md` |
| Wiki Log | `6.Wiki/log.md` |
| Vault 권한 설정 | `.claude/settings.json` |
| 인제스트 스크립트 | `~/scripts/wiki-ingest.sh` |
| 인제스트 로그 | `~/scripts/wiki-ingest.log` |
| Git Hook | `.git/hooks/post-commit` |
| 참조 원문 | [Karpathy LLM Wiki Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) |
