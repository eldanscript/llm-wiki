---
wiki_type: concept
tags: [wiki, llm-wiki, karpathy, knowledge-management, obsidian, ingest]
sources:
  - 2.Areas/KnowledgeBase/OBSIDIAN_WIKI_AGENT.md
  - 2.Areas/KnowledgeBase/Obsidian_Presentation.md
  - 6.Wiki/WIKI_SCHEMA.md
updated: 2026-05-31
---

# LLM Wiki 패턴

Andrej Karpathy가 제안한, **LLM이 Raw 소스를 읽어 합성 지식 페이지를 자동 생성·관리**하는 지식 관리 아키텍처.

---

## 핵심 내용

- **3-Layer 구조**: Raw Sources(불변 원본) → Wiki(LLM 합성) → Schema(운영 규칙) 세 계층이 역할을 분리한다
- **Raw Sources 불변 원칙**: LLM은 원본 노트를 절대 수정하지 않으며, Wiki 계층에만 쓴다
- **Delta 처리**: `.manifest.json`으로 mtime 변경된 파일만 재처리해 중복 인제스트를 방지한다
- **완료 로그**: 각 작업 단계 완료 시 `.done/phase{N}-{timestamp}.log` 파일을 생성해 실행 이력을 보존한다
- **Wikilink 네트워크**: 추출한 개념 간 `[[링크]]`로 지식 그래프를 구성하고, 양방향 역링크를 유지한다
- **Lint(품질 점검)**: 고아 페이지, 깨진 링크, 중복 개념, sources 누락, 오래된 updated 필드를 주기적으로 점검한다

---

## 3-Layer Architecture

| Layer | 위치 | 역할 |
|-------|------|------|
| Raw Sources | `0.Slip-box` ~ `5.Periodic Notes` | 원본 노트 — 절대 수정 금지 |
| Wiki | `6.Wiki/` | LLM이 생성·관리하는 합성 지식 페이지 |
| Schema | `6.Wiki/WIKI_SCHEMA.md` | 구조 규칙 및 운영 가이드 |

---

## 3대 운영 Operations

### Ingest (새 소스 추가)
1. Raw source 읽기 → manifest 델타 확인
2. 신규 개념/엔티티 → Wiki 페이지 생성 또는 병합
3. `index.md` 항목 추가 + `log.md` 기록

### Query (질의 응답)
1. 관련 Wiki 페이지를 읽어 답변
2. 새 인사이트는 해당 Wiki 페이지에 반영
3. 중요 Q&A는 `Topics/`에 신규 페이지로 저장

### Lint (품질 점검)
병렬 서브에이전트 5개로 동시 점검:
- 에이전트 A: concepts/, entities/ 점검
- 에이전트 B: projects/, decisions/ 점검
- 에이전트 C: skills/, references/ 점검
- 에이전트 D: _raw/ 미처리 파일 현황
- 에이전트 E: 전체 wikilink 유효성 검사

---

## Vault 폴더 → Wiki 매핑

| Raw Source | 생성되는 Wiki 페이지 |
|-----------|-------------------|
| `2.Areas/AgenticAI/` | `Concepts/Agentic-AI.md`, `Tools/` 관련 |
| `2.Areas/KnowledgeBase/` | `Concepts/LLM-Wiki-Pattern.md` |
| `2.Areas/AWS/` | `Entities/Companies/AWS.md` |
| `3.Resources/Tech Report/Anthropic Blog/` | `Entities/Companies/Anthropic.md` |

---

## 스킬 연동

이 패턴은 Claude Code 커스텀 스킬로 구현된다:

| 스킬 | 트리거 | 역할 |
|------|--------|------|
| `/적용` | `적용해줘`, `_raw에 있는 것 처리` | Raw 파일 자동 ingest |
| `/위키저장` | `위키저장해줘`, `wiki에 기록해줘` | 대화에서 지식 추출·저장 |
| `/점검` | `점검해줘`, `wiki 상태 확인` | 병렬 Vault 건강 점검 |

자동화: `scripts/auto-wiki.sh`를 cron(매주 월 03:00)으로 스케줄링해 무감독 운영.

---

## 관련 노트

- [[Agentic-AI]] — 이 패턴을 구동하는 AI 운영 패러다임
- [[Multi-Agent-System]] — Lint 단계의 병렬 서브에이전트 패턴
- [[Tools/Claude-Code]] — 스킬·자동화 실행 도구
- [[Tools/QMD]] — Vault 시맨틱 검색 도구

---

## 출처

- `2.Areas/KnowledgeBase/OBSIDIAN_WIKI_AGENT.md` — Obsidian Wiki Agent 실행 지침서
- `2.Areas/KnowledgeBase/Obsidian_Presentation.md` — Obsidian 고급 기능 및 PARA 방법론
- `6.Wiki/WIKI_SCHEMA.md` — 이 Vault의 Wiki 운영 규칙
