# WIKI_SCHEMA — LLM Wiki 운영 규칙

> Karpathy's LLM Wiki 패턴 구현 (2026-05-31)
> Raw sources는 불변 유지 — Wiki만 LLM이 수정한다.

---

## 1. 3-Layer Architecture

| Layer | 위치 | 역할 |
|-------|------|------|
| Raw Sources | `0.Slip-box`, `1.Projects`, `2.Areas`, `3.Resources`, `4.Archive`, `5.Periodic Notes` | 원본 노트 — 절대 수정 금지 |
| Wiki | `6.Wiki/` | LLM이 생성·관리하는 합성 지식 페이지 |
| Schema | `6.Wiki/WIKI_SCHEMA.md` | 구조 규칙 및 운영 가이드 (이 파일) |

---

## 2. Wiki 폴더 구조

```
6.Wiki/
  WIKI_SCHEMA.md      ← 이 파일 (schema)
  index.md            ← 카테고리별 콘텐츠 카탈로그
  log.md              ← append-only 작업 이력
  Projects/           ← 프로젝트 요약 페이지
  Concepts/           ← 추상 개념 (RAG, Agentic AI, LLM 등)
  Entities/
    Companies/        ← 기업 (Anthropic, OpenAI, AWS 등)
    Models/           ← AI 모델 (Claude, GPT-4 등)
    Tools/            ← 소프트웨어 도구
  Topics/             ← 주제별 합성 페이지 (cross-cutting)
```

---

## 3. Wiki 페이지 형식

모든 Wiki 페이지는 아래 frontmatter를 사용한다:

```yaml
---
wiki_type: concept | entity | project | topic
tags: [wiki, <category>]
sources: [링크1, 링크2]   # Raw source 경로
updated: 2026-05-31
---
```

### 페이지 구조 (Concept/Entity)
1. **한 줄 정의** — 무엇인가
2. **핵심 내용** — 3~7개 bullet
3. **관련 노트** — `[[링크]]` 형식
4. **출처** — Raw source 경로

---

## 4. 운영 Operations

### Ingest (새 소스 추가)
1. Raw source를 읽는다
2. 새 개념/엔티티 → 해당 Wiki 페이지 생성 또는 업데이트
3. `index.md` 해당 항목 추가
4. `log.md`에 `[YYYY-MM-DD] INGEST: <소스> → <생성/수정된 페이지들>` 기록

### Query (질의 응답)
1. 질문과 관련된 Wiki 페이지를 읽는다
2. 답변 후 새로운 인사이트는 적절한 Wiki 페이지에 반영
3. 중요한 Q&A는 `Topics/` 에 새 페이지로 저장

### Lint (품질 점검)
점검 항목:
- [ ] 고아 페이지 (index.md에 없는 페이지)
- [ ] 깨진 `[[링크]]`
- [ ] 중복 개념 페이지
- [ ] `sources` 필드가 비어있는 페이지
- [ ] 6개월 이상 `updated` 가 오래된 페이지

---

## 5. Vault → Wiki 매핑

| Raw Source | 생성되는 Wiki 페이지 |
|-----------|-------------------|
| `1.Projects/Raingent/` | `Projects/Raingent.md` |
| `2.Areas/AgenticAI/` | `Concepts/Agentic-AI.md`, `Tools/` 관련 |
| `2.Areas/KnowledgeBase/` | `Concepts/Knowledge-Base.md` |
| `2.Areas/AWS/` | `Entities/Companies/AWS.md`, `Topics/AWS-Summit-2026.md` |
| `2.Areas/FuriosaAI/` | `Entities/Companies/FuriosaAI.md` |
| `3.Resources/Tech Report/Anthropic Blog/` | `Entities/Companies/Anthropic.md` |
| `3.Resources/Tech Report/OpenAI Blog/` | `Entities/Companies/OpenAI.md` |
| `3.Resources/Tech Report/` (기타) | `Entities/Companies/<name>.md` |
| `4.Archive/notion-archive/AI - Self Learning/` | `Concepts/` 관련 |

---

## 6. 크로스 레퍼런스 규칙

- 동일 Wiki 내 링크: `[[파일명]]` (Obsidian 내부 링크)
- Raw source 링크: `[[../2.Areas/AgenticAI/파일명]]`
- 외부 URL: 일반 마크다운 `[텍스트](URL)`
- 모든 Concept 페이지는 관련 Entity를 `[[링크]]`로 연결
- 모든 Entity 페이지는 관련 Concept을 `[[링크]]`로 연결
