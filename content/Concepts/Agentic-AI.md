---
wiki_type: concept
tags: [wiki, agentic-ai, llm, multi-agent, automation]
sources:
  - 2.Areas/AgenticAI/claude_multiagent_guide.md
  - 2.Areas/KnowledgeBase/OBSIDIAN_WIKI_AGENT.md
updated: 2026-05-31
---

# Agentic AI

LLM이 단순 질의응답을 넘어 **자율적으로 계획·실행·도구 사용·협업**을 수행하는 AI 운영 패러다임.

---

## 핵심 내용

- **자율 실행**: 사용자 승인 없이 단계별 판단·실행하며, 실패 시 스스로 대안 접근법을 시도한다
- **도구 사용(Tool Use)**: 파일 시스템, 터미널, API, DB 등 외부 시스템을 직접 호출해 작업을 완수한다
- **역할 분리**: 각 에이전트는 단일 책임(CLAUDE.md 역할 정의)을 가지며, 역할 경계를 지킨다
- **Orchestrator / Subagent 패턴**: 오케스트레이터가 작업을 분해·배분하고, 서브에이전트가 병렬 실행한다 → [[Multi-Agent-System]]
- **완료 신호 프로토콜**: 플래그 파일(`/tmp/backend_done.flag`)이나 로그 파일로 작업 완료·에러를 명시적으로 전달한다
- **컨텍스트 관리**: 긴 세션은 `/compact` 또는 새 세션으로 컨텍스트를 갱신하고, `.claudeignore`로 불필요한 파일을 제외한다

---

## 3-Layer 아키텍처 (Claude Code 팀 기준)

| 레이어 | 구성 | 역할 |
|--------|------|------|
| Layer 3 | 모바일 앱 / Remote-Control API | 지휘 인터페이스 |
| Layer 2 | TMUX 세션 (로컬 머신) | 에이전트 팀 실행 |
| Layer 1 | GitHub · DB · Slack · 파일시스템 | 외부 도구 연동 |

---

## Claude Code 연관성

- **CLAUDE.md** = 에이전트의 직무기술서(JD). 역할·금지사항·완료 신호를 정의한다
- **Remote Control**: `claude --rc "세션명"` 또는 `settings.json: remoteControlAtStartup: true`로 원격 제어 활성화
- **Triple Crown 파이프라인**: gstack → GSD → Superpowers 조합으로 특대형(1주+) 프로젝트 자동화 → [[Tools/gstack]], [[Tools/GSD]]
- **GitHub Actions 통합**: `anthropics/claude-code-action@v1`으로 PR 자동 리뷰 워크플로우 구성
- **Worktree 병렬화**: `git worktree`로 브랜치별 독립 실행 환경 분리, 파인 충돌 방지

---

## 관련 노트

- [[Multi-Agent-System]] — orchestrator/subagent 설계 패턴 상세
- [[LLM-Wiki-Pattern]] — Agentic AI로 운영하는 지식 관리 시스템
- [[Tools/Claude-Code]] — 핵심 실행 도구
- [[Tools/TMUX]] — 에이전트 팀 실행 환경
- [[Tools/gstack]] — 전략·자동화 플러그인
- [[Tools/GSD]] — 마일스톤·페이즈 프로젝트 관리
- [[Tools/RTK]] — 토큰 최적화 도구

---

## 출처

- `2.Areas/AgenticAI/claude_multiagent_guide.md` — Claude Code 멀티에이전트 팀 가이드 (WikiDocs #19736)
- `2.Areas/KnowledgeBase/OBSIDIAN_WIKI_AGENT.md` — Obsidian Wiki Agent 무감독 실행 지침서
