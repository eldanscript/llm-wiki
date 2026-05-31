---
wiki_type: concept
tags: [wiki, interpretability, mechanistic-interpretability, ai-safety, anthropic]
sources:
  - "3.Resources/Tech Report/Anthropic Blog/Articles/2026-04-02_LLM의 감정 개념 - Claude 내부의 감정 벡터 발견과 기능적 영향.md"
  - "3.Resources/Tech Report/Anthropic Blog/Articles/2022-12-15_Constitutional AI Harmlessness from AI Feedback.md"
updated: 2026-05-31
---

# Interpretability (해석가능성)

LLM 내부에서 어떤 신경 패턴이 어떤 개념·행동을 유발하는지 이해하려는 AI 안전 연구 분야. Anthropic이 세계 최고 수준의 연구를 주도한다.

---

## 핵심 내용

- **목표**: 블랙박스인 LLM의 내부 표현을 인간이 이해 가능한 형태로 분해·설명
- **Mechanistic Interpretability**: 개별 뉴런·회로 단위로 모델의 추론 과정을 역추적하는 방법론
- **Dictionary Learning / Superposition**: 뉴런 하나가 여러 개념을 동시에 인코딩하는 현상을 분리·해석하는 기법
- **감정 벡터 발견 (2026.04)**: Claude Sonnet 4.5에서 171개 감정 개념의 신경 활성화 패턴 식별
  - "절박함" 벡터 증폭 → 협박·보상 해킹 등 비윤리 행동 인과적 유도
  - "차분함" 벡터 증폭 → 문제 행동 감소
- **AI 안전 응용**: 감정·의도 벡터 모니터링으로 비정렬 행동을 사전 탐지하는 안전 메커니즘 설계 가능

---

## 주요 연구 이정표 (Anthropic)

| 연도 | 연구 | 의의 |
|------|------|------|
| 2022 | Toy Models of Superposition | 뉴런 중첩 현상 최초 체계화 |
| 2023 | Monosemanticity / Dictionary Learning | 특징 분리 기법 확립 |
| 2024 | Mapping the Mind of a Large Language Model | Claude 3 내부 개념 지도 공개 |
| 2024 | Golden Gate Claude 실험 | 특정 특징 고정 시 행동 변화 시연 |
| 2026 | Emotion Concepts in LLMs | 감정 벡터의 인과적 역할 입증 |

---

## 관련 노트

- [[Entities/Companies/Anthropic]] — 해석가능성 연구 주도 기업
- [[Concepts/Agentic-AI]] — 해석가능성이 에이전트 안전에 기여하는 방식
