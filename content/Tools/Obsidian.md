---
wiki_type: entity
tags: [wiki, tools, obsidian, pkm, knowledge-base]
sources:
  - "[[../../1.Projects/Raingent/Migration/Obsidian Sync]]"
  - "[[../../1.Projects/Raingent/Migration/Obsidian 최적화]]"
  - "[[../../1.Projects/Raingent/Migration/Tech Report Agent]]"
updated: 2026-05-31
---

# Obsidian

Markdown 기반 로컬 우선 PKM(Personal Knowledge Management) 도구. Raingent에서는 AI 에이전트가 생성하는 Tech Report와 개인 노트를 통합 관리하는 중앙 지식 저장소로 사용.

---

## 핵심 내용

- **Vault 경로**: Ubuntu `~/문서/Obsidian Vault`, MacBook `~/Documents/Obsidian Vault`
- **동기화**: GitHub Private 저장소 (`eldanscript/obsidian-vault`) + Obsidian Git 플러그인 (10분 자동 커밋·푸시)
- **멀티 디바이스 역할 분리**: Ubuntu → Tech Report 자동 수집(쓰기), MacBook → 노트 편집(읽기+쓰기)
- **충돌 방지**: MacBook은 `Pull strategy: rebase` + `Pull on startup: ON`, Tech Report 폴더는 MacBook에서 수정 금지
- **LLM Wiki**: `6.Wiki/` 폴더에 Karpathy's LLM Wiki 패턴으로 AI가 관리하는 합성 지식 계층 추가

## 플러그인

- **Obsidian Git**: 자동 커밋·푸시·풀 (10분 간격)

## Git 설정

```bash
git -C ~/문서/Obsidian\ Vault config user.name "eldanscript"
git -C ~/문서/Obsidian\ Vault config user.email "eldanscript@gmail.com"
```

## .gitignore 권장 항목

```
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/cache
.DS_Store
.trash/
```

---

## 관련 노트

- [[../Projects/Raingent]]
- [[Tech-Report-Agent]]
