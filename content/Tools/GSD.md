---
wiki_type: entity
tags: [wiki, tool, gsd, project-management, milestone, phase, claude-code]
sources:
  - 2.Areas/AgenticAI/claude_multiagent_guide.md
updated: 2026-05-31
---

# GSD (Get Stuff Done)

Claude Code용 **마일스톤·페이즈 기반 프로젝트 관리 도구**. 복잡한 작업을 페이즈로 구조화하고 단계별 실행·검증을 자동화한다.

---

## 핵심 내용

- **페이즈 구조화**: 프로젝트를 마일스톤 → 페이즈로 분해해 실행 순서와 의존성을 명확히 한다
- **실행 자동화**: `/gsd:execute-phase`로 현재 페이즈의 모든 태스크를 에이전트가 순차/병렬 실행
- **Superpowers 연동**: TDD·리팩터링 등 방법론 스킬을 페이즈 실행에 주입한다
- **Triple Crown 중간 담당**: [[Tools/gstack]]이 전략을 수립하면 GSD가 구조화·구현·검증(2~4단계)을 처리

---

## 핵심 명령어

| 명령 | 역할 |
|------|------|
| `/gsd:new-project` | 신규 프로젝트 생성 |
| `/gsd:plan-phase` | 페이즈 계획 수립 |
| `/gsd:execute-phase` | 현재 페이즈 실행 |
| `/gsd:validate` | 페이즈 결과 검증 |
| `/gsd:complete-milestone` | 마일스톤 완료 처리 |

---

## Triple Crown 5단계에서의 역할

| Phase | GSD 역할 |
|-------|----------|
| 2. 구조화 | `/gsd:new-project → /gsd:plan-phase` |
| 3. 구현 | `/gsd:execute-phase` (+ Superpowers TDD 스킬) |
| 4. 검증 | `/gsd:validate` |
| 5. 완료 | `/gsd:complete-milestone` |

---

## 관련 노트

- [[Multi-Agent-System]] — GSD 페이즈를 서브에이전트에게 병렬 위임
- [[Tools/gstack]] — Triple Crown의 전략 수립·완료 단계 담당
- [[Tools/Claude-Code]] — GSD가 실행되는 플랫폼

---

## 출처

- `2.Areas/AgenticAI/claude_multiagent_guide.md` — Ch06 플러그인 스택, Ch07 Triple Crown 파이프라인
