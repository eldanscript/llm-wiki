---
wiki_type: concept
tags: [wiki, multi-agent, orchestrator, subagent, parallel, claude-code]
sources:
  - 2.Areas/AgenticAI/claude_multiagent_guide.md
  - 2.Areas/KnowledgeBase/OBSIDIAN_WIKI_AGENT.md
updated: 2026-05-31
---

# Multi-Agent System

**여러 AI 에이전트가 역할을 분담해 병렬·협력 실행**하는 시스템. 단일 에이전트로는 처리 불가한 복잡하고 큰 작업을 분해·위임해 완수한다.

---

## 핵심 내용

- **역할 격리**: 각 에이전트는 CLAUDE.md로 정의된 단일 책임을 가지며, 다른 역할 영역(예: `frontend/` 디렉토리) 접근을 금지한다
- **Orchestrator**: 전체 작업을 분해하고 서브에이전트에게 배분·모니터링하며, 결과를 통합한다
- **Subagent**: 오케스트레이터로부터 위임받은 단위 작업을 독립 실행하고, 완료 신호로 결과를 보고한다
- **병렬 실행**: TMUX 파인 또는 Git Worktree로 여러 에이전트가 동시에 다른 브랜치·디렉토리에서 작업한다
- **완료 신호 프로토콜**: 플래그 파일(`touch /tmp/backend_done.flag`) 또는 에러 로그(`echo "에러" > /tmp/backend_error.log`)로 상태를 명시적 전달
- **컨텍스트 격리**: 에이전트 간 충돌 방지를 위해 `git worktree`로 브랜치별 독립 작업 환경을 구성한다

---

## Orchestrator / Subagent 패턴

```
사람(또는 오케스트레이터 에이전트)
    ├── TMUX pane 0 → Orchestrator  (전략·배분)
    ├── TMUX pane 1 → PM·아키텍트   (설계)
    ├── TMUX pane 2 → 리서처        (조사)
    ├── TMUX pane 3 → 백엔드 개발자  (구현)
    ├── TMUX pane 4 → 프론트엔드    (구현)
    └── TMUX pane 5 → 리뷰어        (검증)
```

---

## 5+5 병렬 운영 패턴

| 구분 | 인스턴스 수 | 역할 예시 |
|------|------------|----------|
| 로컬 TMUX | 5개 파인 | 오케스트레이터, 백엔드A/B, 프론트, 리뷰어 |
| 클라우드 | 5~10개 세션 | 리서치, 문서화, 테스트, 코드리뷰, 성능분석 |

---

## 작업 규모별 적용 기준

| 규모 | 권장 도구 | 예시 |
|------|----------|------|
| 소 (1h 이내) | 도구 없이 | 오타 수정 |
| 중 (반나절) | gstack만 | 버그 수정 |
| 대 (1~3일) | gstack + Superpowers | 새 API 모듈 |
| 특대 (1주+) | Triple Crown 전체 | 신규 서비스 |

**Triple Crown** = gstack(`/cso → /autoplan`) + GSD(`/gsd:new-project → /gsd:execute-phase`) + Superpowers(TDD 스킬 주입)

---

## Lint에서의 병렬 서브에이전트 (LLM Wiki 패턴)

[[LLM-Wiki-Pattern]]의 `/점검` 스킬도 동일 패턴 적용:

```
Main Agent (점검 조율)
    ├── Subagent A → concepts/, entities/ 점검
    ├── Subagent B → projects/, decisions/ 점검
    ├── Subagent C → skills/, references/ 점검
    ├── Subagent D → _raw/ 미처리 파일 현황
    └── Subagent E → 전체 wikilink 유효성 검사
```

---

## 관련 노트

- [[Agentic-AI]] — 멀티에이전트의 상위 개념
- [[LLM-Wiki-Pattern]] — 멀티에이전트를 Vault 관리에 적용한 사례
- [[Tools/Claude-Code]] — 에이전트 실행 도구
- [[Tools/TMUX]] — 에이전트 팀 실행 환경 (파인 레이아웃)
- [[Tools/gstack]] — 오케스트레이터 전략 도구
- [[Tools/GSD]] — 페이즈별 작업 관리

---

## 출처

- `2.Areas/AgenticAI/claude_multiagent_guide.md` — Ch01~08, 특히 팀 구성·병렬 운용·Triple Crown
- `2.Areas/KnowledgeBase/OBSIDIAN_WIKI_AGENT.md` — Phase 2-3의 병렬 서브에이전트 설계
