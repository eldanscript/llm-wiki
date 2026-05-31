---
wiki_type: entity
tags: [wiki, tool, gstack, plugin, strategy, automation, claude-code]
sources:
  - 2.Areas/AgenticAI/claude_multiagent_guide.md
updated: 2026-05-31
---

# gstack

Claude Code용 **플러그인 스택 매니저 + 전략 자동화 도구**. 프로젝트 전략 수립부터 배포까지의 파이프라인을 슬래시 명령어로 조율한다.

---

## 핵심 내용

- **전략 자동화**: `/cso`(Chief Strategy Officer 모드)로 프로젝트 방향 분석, `/autoplan`으로 실행 계획 자동 생성
- **Triple Crown 진입점**: [[Tools/GSD]], Superpowers와 함께 특대형(1주+) 프로젝트의 1단계(전략 수립)와 5단계(완료)를 담당
- **플러그인 스택 관리**: Superpowers, GSD 등 다른 도구들의 조합을 중앙에서 관리
- **소·중형 작업**: 중 규모(반나절) 작업은 gstack만으로도 충분히 처리 가능

---

## 핵심 명령어

| 명령 | 역할 |
|------|------|
| `/cso` | Chief Strategy Officer 모드 — 전략 분석 |
| `/autoplan` | 프로젝트 실행 계획 자동 생성 |
| `/ship` | 배포 완료 처리 |
| `/review` | 코드 리뷰 자동화 |
| `/qa` | QA 검증 |

---

## Triple Crown 5단계에서의 역할

| Phase | gstack 역할 |
|-------|------------|
| 1. 전략 수립 | `/cso → /autoplan` |
| 4. 검증 | `/review → /qa` |
| 5. 완료 | `/ship` |

---

## 관련 노트

- [[Multi-Agent-System]] — Triple Crown 파이프라인의 오케스트레이터 역할
- [[Tools/GSD]] — 2~4단계를 담당하는 프로젝트 관리 도구
- [[Tools/Claude-Code]] — gstack이 실행되는 플랫폼

---

## 출처

- `2.Areas/AgenticAI/claude_multiagent_guide.md` — Ch06 플러그인 스택, Ch07 Triple Crown 파이프라인
