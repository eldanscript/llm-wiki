---
wiki_type: entity
tags: [wiki, tool, claude-code, anthropic, cli, agentic-ai, hooks]
sources:
  - 2.Areas/AgenticAI/claude_multiagent_guide.md
  - 2.Areas/AgenticAI/claude_hooks_guide.md
  - 2.Areas/KnowledgeBase/Obsidian_Presentation.md
  - "[[../../1.Projects/Raingent/Migration/FM Setup]]"
  - "[[../../1.Projects/Raingent/Migration/Claude Code Clone Agent]]"
  - "[[../../1.Projects/Raingent/Migration/Frontier Model 구독]]"
updated: 2026-05-31
---

# Claude Code

Anthropic이 제공하는 **터미널 기반 AI 코딩 어시스턴트 CLI**. 파일 시스템·터미널·외부 도구를 직접 제어하며 Agentic AI 팀의 핵심 실행 단위로 동작한다.

---

## 핵심 내용

- **설치**: `npm install -g @anthropic-ai/claude-code` / 인증: `claude auth login` (OAuth, claude.ai 계정 필수)
- **CLAUDE.md**: 에이전트의 직무기술서(JD). 역할·담당 업무·금지 사항·완료 신호를 정의한다
- **Remote Control**: `claude --rc "세션명"` 또는 `settings.json: remoteControlAtStartup: true`로 모바일·원격 제어 활성화
- **스킬 시스템**: `.skills/` 폴더에 커스텀 슬래시 명령어를 정의해 반복 작업을 자동화한다
- **Hooks**: `settings.json`에 정의하는 이벤트 기반 자동화 시스템. 도구 실행 전후에 쉘 명령을 삽입한다 (→ [[#Hooks 이벤트]]) 
- **GitHub Actions**: `anthropics/claude-code-action@v1`으로 PR 자동 리뷰 워크플로우 구성

---

## 주요 명령어

| 명령 | 설명 |
|------|------|
| `claude auth login` | OAuth 인증 |
| `claude --rc "세션명"` | Remote Control 모드 시작 |
| `/compact` | 컨텍스트 압축 |
| `/remote-control` | 현재 세션에서 RC 활성화 |

---

## Hooks 이벤트

`settings.json`의 `hooks` 키에 이벤트별 쉘 명령을 등록한다.

| 이벤트 | 타이밍 | 주요 활용 |
|--------|--------|-----------|
| `PreToolUse` | 도구 실행 직전 | 입력 검증, 로깅, 차단 (`exit 2`로 도구 호출 취소) |
| `PostToolUse` | 도구 실행 직후 | 결과 후처리, 알림 |
| `Stop` | Claude 응답 완료 후 | 요약 저장, 커밋 자동화 |
| `Notification` | 사용자 입력 대기 시 | Slack·텔레그램 외부 알림 |

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write",
      "hooks": [{"type": "command", "command": "echo 파일저장 >> ~/logs/writes.log"}]
    }],
    "Stop": [{
      "hooks": [{"type": "command", "command": "bash ~/scripts/notify.sh"}]
    }]
  }
}
```

**주의사항**
- 훅 스크립트 오류는 Claude 실행을 중단시킬 수 있음
- `PreToolUse`에서 `exit 2` 반환 시 해당 도구 호출을 차단함
- 무거운 작업은 백그라운드(`&`)로 분리 권장
- [[Tools/RTK]]는 `PreToolUse` 훅으로 구현된 대표 사례 (응답 토큰 평균 63% 절약)

---

## settings.json 보안 예시

```json
{
  "remoteControlAtStartup": true,
  "permissions": {
    "allow": ["Bash(git status)", "Bash(git diff*)", "Read"],
    "deny":  ["Bash(rm -rf*)", "Bash(git push --force*)"]
  }
}
```

---

## Raingent 운영 설정 (FM Setup)

- **현재 인증**: Claude Pro 연간 구독 (rainbell72@gmail.com) — Bedrock에서 전환
- **Bedrock 설정 제거 시**: `settings.json`에서 `CLAUDE_CODE_USE_BEDROCK`, `AWS_REGION` 등 삭제 후 `/logout` → 재로그인
- **비용 최적화 권장 설정**:

```json
{
  "env": {
    "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "70",
    "DISABLE_NON_ESSENTIAL_MODEL_CALLS": "1"
  },
  "verbose": false,
  "spinnerTipsEnabled": false
}
```

- **GCP 연동**: Google AI Studio (eldanscript@gmail.com), Gemini CLI 1K req/day 무료
- **Azure 연동**: raingent-openai-endpoint.openai.azure.com

---

## 관련 노트

- [[Agentic-AI]] — Claude Code가 구현하는 AI 운영 패러다임
- [[Multi-Agent-System]] — 팀 에이전트 구성
- [[Tools/TMUX]] — Claude Code 다중 인스턴스 실행 환경
- [[Tools/gstack]] — Claude Code 플러그인 스택
- [[Tools/RTK]] — Claude Code 토큰 최적화

---

## 출처

- `2.Areas/AgenticAI/claude_multiagent_guide.md` — Ch02~09 설치·운영·트러블슈팅
- `2.Areas/KnowledgeBase/Obsidian_Presentation.md` — Obsidian-Claude Code 연동
