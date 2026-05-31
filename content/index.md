# Wiki Index

> LLM이 관리하는 지식 카탈로그. Agent 인제스트 완료 후 자동 갱신됨.
> Schema: [[WIKI_SCHEMA]] | Log: [[log]]
> 마지막 갱신: 2026-05-31 (Agent0~3 전체 인제스트 완료)

---

## Projects

- [[Projects/Raingent]] — Ubuntu PC 기반 개인 AI 에이전트 생태계 (Finance Agent, Tech Report, Naver Blog 등)

---

## Concepts

- [[Concepts/Agentic-AI]] — LLM이 자율적으로 계획·실행·도구 사용·협업을 수행하는 AI 운영 패러다임
- [[Concepts/LLM-Wiki-Pattern]] — Karpathy의 LLM이 Raw 소스를 읽어 합성 지식 페이지를 자동 생성·관리하는 아키텍처
- [[Concepts/Multi-Agent-System]] — 여러 AI 에이전트가 역할을 분담해 병렬·협력 실행하는 시스템

---

## Entities

### Companies

- [[Entities/Companies/Anthropic]] — 2021년 설립 AI 안전 연구 기업. Claude 모델 시리즈 개발사, Constitutional AI·Interpretability 연구 선도
- [[Entities/Companies/FuriosaAI]] — 한국 AI 반도체 스타트업. RNGD(RENEGADE) NPU 개발·양산, TCP 아키텍처로 에너지 효율 특화

### Models

_인제스트 대기 중_

### Tools

- [[Tools/Claude-Code]] — Anthropic 터미널 AI 코딩 CLI, Raingent 에이전트 핵심 실행 단위 (Hooks 이벤트 시스템 포함)
- [[Tools/Obsidian]] — Markdown PKM 도구, Raingent 지식 저장소 (GitHub 동기화)
- [[Tools/Tailscale]] — WireGuard 기반 Mesh VPN, MacBook ↔ Ubuntu PC 원격 접속
- [[Tools/Finance-Agent]] — 자산 모니터링·자동 매수 Python 에이전트
- [[Tools/Tech-Report-Agent]] — GenAI 기술 블로그 자동 수집·요약 에이전트
- [[Tools/GSD]] — Claude Code용 마일스톤·페이즈 기반 프로젝트 관리 도구 (Get Stuff Done)
- [[Tools/QMD]] — Obsidian Vault 시맨틱 검색 CLI 도구, 의미 기반 노트 탐색
- [[Tools/RTK]] — Claude Code CLI 출력 토큰 최적화 도구, PreToolUse 훅으로 평균 63% 절약
- [[Tools/TMUX]] — 터미널 멀티플렉서, 파인 분할로 Claude Code 에이전트 팀 병렬 실행 환경
- [[Tools/gstack]] — Claude Code용 플러그인 스택 매니저 + 전략 자동화 도구, Triple Crown 진입점

---

## Topics

- [[Topics/AWS-Summit-Seoul-2026]] — AWS Summit Seoul 2026 주요 발표: 에이전틱 AI·서버리스·Bedrock AgentCore 중심
- [[Topics/NPU-AI-Chip-Landscape]] — NPU/AI 칩 생태계 비교: FuriosaAI RNGD vs NVIDIA GPU vs AWS Trainium, 에너지 효율 트렌드
