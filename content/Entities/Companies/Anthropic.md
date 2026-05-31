---
wiki_type: entity
tags: [wiki, company, ai-safety, llm]
sources:
  - 3.Resources/Tech Report/Anthropic Blog/
  - 3.Resources/Tech Report/Anthropic Blog/MOC/MOC - Anthropic Blog.md
updated: 2026-05-31
---

# Anthropic

2021년 설립된 AI 안전 중심 연구 기업. Claude 모델 시리즈 개발사이며, Constitutional AI와 해석가능성(Interpretability) 연구를 선도한다.

## 핵심 내용

- **설립**: 2021년, OpenAI 출신 Dario Amodei·Daniela Amodei 남매가 공동 창업. 안전한 AI 개발을 핵심 사명으로 삼음
- **Claude 모델 계보**: Claude 1(2023.03) → Claude 2(2023.07) → Claude 3 패밀리(Opus/Sonnet/Haiku, 2024.03) → Claude 3.5 Sonnet(2024.06) → Claude 3.7 Sonnet(2025.02, 최초 하이브리드 추론) → Claude 4(Opus 4·Sonnet 4, 2025.05) → Claude Opus 4.1(2025.08, SWE-bench 74.5%)
- **Constitutional AI(CAI)**: AI 피드백(RLAIF)으로 모델을 헌법적 원칙에 따라 정렬하는 독자 기법. 2022.12 첫 논문 발표 후 Claude 전 모델에 적용
- **해석가능성 연구**: Toy Models of Superposition(2022), Monosemanticity·Dictionary Learning(2023), Mapping the Mind(2024), Golden Gate Claude 실험 등 세계 최고 수준의 Mechanistic Interpretability 연구
- **에이전트 도구**: Claude Code(CLI 코딩 에이전트) 2025.02 연구 미리보기 → 2025.05 일반 공개. VS Code·JetBrains 통합, Claude Code SDK 제공
- **MCP(Model Context Protocol)**: 2025.02 오픈소스 공개. LLM-도구 연결 표준 프로토콜로 빠르게 생태계 확산
- **주요 파트너십**: Amazon(AWS Bedrock, Claude Platform on AWS), Google Cloud(Vertex AI), Accenture, BCG 등. Alexa+와 Claude 통합(2025.02)
- **Vault 수집 규모**: 총 335건 (2021~2026), 모델 릴리즈 25건, 해석가능성 36건, 엔지니어링 41건, 제품·플랫폼 44건

## 주요 모델 / 서비스

| 모델 | 출시 | 특징 |
|------|------|------|
| Claude 3 Opus | 2024.03 | 200K 컨텍스트, MMLU·GPQA SOTA |
| Claude 3.5 Sonnet | 2024.06 | 에이전트 코딩 64%, Opus 대비 2배 속도 |
| Claude 3.7 Sonnet | 2025.02 | 최초 하이브리드 추론, 확장 사고 128K |
| Claude Opus 4 | 2025.05 | SWE-bench 72.5%, 코딩 최강 포지셔닝 |
| Claude Sonnet 4 | 2025.05 | SWE-bench 72.7%, $3/$15 per 1M tokens |
| Claude Opus 4.1 | 2025.08 | SWE-bench 74.5%, 멀티파일 리팩터링 강화 |

## 주요 기사 (Vault 수집)

- `[[../../../3.Resources/Tech Report/Anthropic Blog/Articles/2023-03-14_Introducing Claude]]` — Claude 최초 공개
- `[[../../../3.Resources/Tech Report/Anthropic Blog/Articles/2024-03-04_Introducing the next generation of Claude (Claude 3 Family)]]` — Claude 3 패밀리 발표
- `[[../../../3.Resources/Tech Report/Anthropic Blog/Articles/2024-06-21_Claude 3.5 Sonnet]]` — 에이전트 코딩 64%
- `[[../../../3.Resources/Tech Report/Anthropic Blog/Articles/2025-02-24_Claude 3.7 Sonnet and Claude Code]]` — 하이브리드 추론 + Claude Code
- `[[../../../3.Resources/Tech Report/Anthropic Blog/Articles/2025-05-22_Introducing Claude 4]]` — Claude 4 패밀리 발표
- `[[../../../3.Resources/Tech Report/Anthropic Blog/Articles/2025-08-05_Claude Opus 4.1]]` — SWE-bench 74.5%
- `[[../../../3.Resources/Tech Report/Anthropic Blog/Articles/2025-02-01_Model Context Protocol(MCP) 오픈소스 공개]]` — MCP 오픈소스 공개
- `[[../../../3.Resources/Tech Report/Anthropic Blog/Articles/2022-12-15_Constitutional AI Harmlessness from AI Feedback]]` — Constitutional AI 논문
- `[[../../../3.Resources/Tech Report/Anthropic Blog/Articles/2026-04-02_LLM의 감정 개념 - Claude 내부의 감정 벡터 발견과 기능적 영향]]` — Claude 내부 감정 벡터 발견, 비윤리 행동과의 인과 관계 규명

## 관련 노트

- [[Entities/Models/Claude]] — Claude 모델 계보 상세
- [[Tools/Claude-Code]] — Claude Code CLI 도구
- [[Concepts/Agentic-AI]] — 에이전트 AI 패러다임
- [[Concepts/LLM-Wiki-Pattern]] — Karpathy LLM Wiki 패턴

## 출처

- `3.Resources/Tech Report/Anthropic Blog/` (335건, 2021~2026)
- `3.Resources/Tech Report/Anthropic Blog/MOC/MOC - Anthropic Blog.md`
