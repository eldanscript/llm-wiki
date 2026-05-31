---
wiki_type: entity
tags: [wiki, tool, qmd, semantic-search, obsidian, knowledge-base, markdown]
sources:
  - 2.Areas/KnowledgeBase/Obsidian_Presentation.md
updated: 2026-05-31
---

# QMD (Query Markdown Documents)

Obsidian Vault를 **시맨틱 검색**하는 CLI 도구. 키워드 매칭이 아닌 의미 기반으로 관련 노트를 찾아 [[LLM-Wiki-Pattern]]의 Query·Lint 단계에서 활용된다.

---

## 핵심 내용

- **시맨틱 검색**: 임베딩 기반으로 의미적으로 유사한 노트 탐색 (`qmd vsearch "zettelkasten" --files`)
- **컬렉션 관리**: 볼트 폴더를 컬렉션으로 등록해 인덱싱
- **영구 보관 노트 작성 스킬 연동**: Claude Code의 `permanent-note` 스킬에서 연관 노트 탐색에 QMD MCP 서버 활용 권장
- **Obsidian Dataview와 상호보완**: Dataview가 메타데이터·구조 쿼리라면, QMD는 내용 기반 시맨틱 검색

---

## 설치 및 사용

```bash
npm install -g @tobilu/qmd
qmd collection add . --name PKM_personal   # 볼트 등록
qmd embed                                   # 임베딩 생성
qmd status                                  # 인덱스 상태 확인
qmd vsearch "zettelkasten" --files          # 시맨틱 검색
```

---

## 관련 노트

- [[LLM-Wiki-Pattern]] — Wikilink 네트워크 구성 시 관련 노트 탐색에 활용
- [[Agentic-AI]] — Claude Code 스킬에서 QMD MCP 서버로 호출

---

## 출처

- `2.Areas/KnowledgeBase/Obsidian_Presentation.md` — QMD 구축 및 영구 보관 노트 스킬 연동
