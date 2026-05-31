---
wiki_type: entity
tags: [wiki, tools, tech-report-agent, automation, genai, research]
sources:
  - "[[../../1.Projects/Raingent/Migration/Tech Report Agent]]"
  - "[[../../1.Projects/Raingent/Migration/Obsidian 최적화]]"
updated: 2026-05-31
---

# Tech Report Agent

GenAI 주요 기술 블로그를 자동 수집·요약하여 Obsidian Vault에 저장하는 에이전트. Ubuntu PC에서 24/7 운영 목표.

---

## 핵심 내용

- **목적**: 주요 AI 기업 블로그에서 핵심 기술 동향 자동 파악 및 심층 리서치
- **수집 소스**: openai, anthropic, deepmind, google-ai, meta-ai, nvidia, microsoft, apple-ml, huggingface, tldr-ai, import-ai, last-week-in-ai, the-decoder
- **저장 위치**: `/media/rainny/FAT/anthropic-blog/` (외장 드라이브), Obsidian Vault 연동
- **Obsidian 연동**: Tech Report 수집 결과 → `3.Resources/Tech Report/` 하위 자동 커밋·푸시
- **상태**: In Progress (Obsidian Vault 연동 설계 중)
- **멀티 디바이스 역할**: Ubuntu PC(자동 쓰기) → GitHub → MacBook(읽기 전용)

---

## 관련 노트

- [[../Projects/Raingent]]
- [[Obsidian]]
- [[Claude-Code]]
