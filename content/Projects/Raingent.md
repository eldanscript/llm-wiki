---
wiki_type: project
tags: [wiki, projects, raingent, ai-agents, ubuntu]
sources:
  - "[[../../1.Projects/Raingent/Migration/Raingent Setup]]"
  - "[[../../1.Projects/Raingent/Migration/PC 환경 구성]]"
  - "[[../../1.Projects/Raingent/Migration/Finance Agent Update]]"
  - "[[../../1.Projects/Raingent/Migration/Tech Report Agent]]"
  - "[[../../1.Projects/Raingent/Migration/Claude Code Clone Agent]]"
  - "[[../../1.Projects/Raingent/Migration/OpenClaw - Jetson]]"
  - "[[../../1.Projects/Raingent/Migration/Naver Blog]]"
  - "[[../../1.Projects/Raingent/Migration/Frontier Model 구독]]"
  - "[[../../1.Projects/Raingent/Migration/원격 접속 설정]]"
  - "[[../../1.Projects/Raingent/Migration/Obsidian Sync]]"
  - "[[../../1.Projects/Raingent/Migration/Work Tracker Template Database]]"
updated: 2026-05-31
---

# Raingent

Ubuntu PC 기반 개인 AI 에이전트 생태계. MacBook에서 구축한 AI 에이전트들을 Ubuntu PC로 이전하고, 24/7 자동화 워크플로우를 구축하는 프로젝트.

---

## 목적

- Frontier Model(Claude/Gemini/GPT)을 활용한 개인 AI 에이전트 팀 구축
- MacBook → Ubuntu PC 마이그레이션 및 24/7 자율 운영
- Tech Report 자동 수집, 금융 자산 모니터링, 블로그 자동 생성 등 실용 자동화

---

## PC 환경

| 기기 | 역할 | Tailscale IP |
|------|------|--------------|
| Ubuntu 24.04 LTS (`rainny-ubuntu-24`) | 메인 에이전트 서버 (24/7) | 100.122.69.43 |
| MacBook Pro (`griffy-macbook-pro`) | 노트 작성·개발 | 100.124.68.115 |

- 두 기기는 [[../Tools/Tailscale]] VPN으로 연결, 포트 포워딩 불필요
- Ubuntu PC 원격 접속: `tailscale ssh rainny@rainny-ubuntu-24` 또는 VNC (`vnc://100.122.69.43:5900`)
- 외장 드라이브 마운트: `/media/rainny/FAT` (exFAT, UUID=6339-9566)

---

## 구성 요소 (서브 프로젝트)

| 프로젝트 | 상태 | 우선순위 | 설명 |
|----------|------|----------|------|
| [[../Tools/Finance-Agent]] | In Progress | High | 자산 주간 보고(이메일), 주식 일일 알림(텔레그램), 자동 매수 |
| [[../Tools/Tech-Report-Agent]] | In Progress | Medium | GenAI 주요 블로그 자동 수집·요약 → Obsidian |
| Claude Code Clone Agent | To Do | High | Claude Code 소스 분석 및 프레임워크 클론 |
| [[Naver Blog Agent]] | To Do | High | AI 블로그 자동 생성·게시로 광고 수익 확보 |
| OpenClaw / Jetson | To Do | High | Jetson에 로컬 LLM 배포, K8s 기반 에이전트 프레임워크 |
| Rainny Bot | To Do | High | (목표 미정의) |
| Research - NPU | To Do | Low | NPU/AI 칩 기술 동향 연구 |

---

## 연동 서비스

### Frontier Models
- **Claude**: Pro 연간 구독 (rainbell72@gmail.com), 설정 파일 `~/.claude/settings.json`
  - Bedrock, GCP(Vertex AI), Azure 모두 연결 가능
- **Gemini**: Google AI Studio API Key (eldanscript + rainbell72 계정 각각)
- **GPT**: Azure OpenAI endpoint (`raingent-openai-endpoint.openai.azure.com`)

### Google 서비스
- **Gmail API**: GCP 프로젝트 `raingent`, OAuth 앱 `raingent-desktop`
  - 인증 계정: eldanscript@gmail.com, rainbell72@gmail.com
  - Scope: `gmail.modify`
  - 토큰 위치: `/home/rainny/raingent/credentials/{account}/token.json`

### 지식 관리
- **Obsidian Vault**: [[../Tools/Obsidian]] — GitHub 저장소 `eldanscript/obsidian-vault` 로 멀티 디바이스 동기화
- **Tech Report 저장소**: `/media/rainny/FAT/anthropic-blog/` (외장 드라이브)

---

## 현황 (2026-05-31)

- **마이그레이션 단계**: Notion 노트 → Obsidian 이전 완료, 에이전트 MacBook → Ubuntu 이전 진행 중
- Finance Agent: Ubuntu PC로 이전 중 (`evaluation.zip`)
- Tech Report Agent: Obsidian Vault 연동 설계 중
- Claude Code Clone: 소스 분석 저장소 생성 (`eldanscript/AllAroundAgent`)
- Naver Blog Agent: 멀티 에이전트 설계 단계 (Trend 분석 → 자료 수집 → 블로그 생성 → 게시)

---

## 관련 노트

- [[../Tools/Claude-Code]]
- [[../Tools/Obsidian]]
- [[../Tools/Tailscale]]
- [[../Tools/Finance-Agent]]
- [[../Tools/Tech-Report-Agent]]
