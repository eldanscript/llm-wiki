---
wiki_type: entity
tags: [wiki, tool, rtk, token-optimization, cli, hooks, claude-code]
sources:
  - 2.Areas/AgenticAI/claude_multiagent_guide.md
updated: 2026-05-31
---

# RTK (Response Token Kit)

Claude Code의 **CLI 출력 토큰을 최적화**하는 도구. PreToolUse 훅으로 Bash 명령 실행 전 출력을 압축해 평균 63% 토큰 절약 효과를 낸다.

---

## 핵심 내용

- **평균 63% 토큰 절약**: CLI 출력에서 불필요한 공백·반복·장황한 로그를 압축 처리
- **Hooks 기반 동작**: Claude Code `settings.json`의 `PreToolUse` 훅에 등록해 Bash 도구 실행마다 자동 개입
- **비침투적 통합**: 에이전트 코드 변경 없이 설정 파일 수정만으로 적용 가능
- `rtk gain`: 현재 세션 토큰 절약량 리포트
- `rtk discover`: 최적화 가능한 패턴 탐색

---

## 설치 및 설정

```json
// ~/.claude/settings.json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{"type": "command", "command": "~/.local/bin/rtk-hook"}]
    }]
  }
}
```

```bash
rtk gain       # 절약량 확인
rtk discover   # 최적화 패턴 탐색
```

---

## 관련 노트

- [[Tools/Claude-Code]] — RTK가 훅으로 통합되는 플랫폼
- [[Multi-Agent-System]] — 다중 에이전트 환경에서 토큰 비용 절감에 중요

---

## 출처

- `2.Areas/AgenticAI/claude_multiagent_guide.md` — Ch06 플러그인 스택 (RTK 섹션)
