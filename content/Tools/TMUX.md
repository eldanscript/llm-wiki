---
wiki_type: entity
tags: [wiki, tool, tmux, terminal, multiplexer, multi-agent]
sources:
  - 2.Areas/AgenticAI/claude_multiagent_guide.md
updated: 2026-05-31
---

# TMUX

**터미널 멀티플렉서**. 하나의 터미널 세션을 여러 파인(pane)으로 분할해 Claude Code 에이전트 팀을 동시 실행하는 핵심 인프라.

---

## 핵심 내용

- **파인(Pane)**: 각 파인이 독립된 Claude Code 인스턴스를 실행, 역할별로 분리된 에이전트 환경 제공
- **세션 영속성**: SSH 연결이 끊겨도 세션이 유지되며 `tmux attach -t team`으로 재접속
- **send-keys**: `tmux send-keys -t team:0.1 "명령" Enter`로 외부에서 특정 파인에 명령 전송
- **capture-pane**: `tmux capture-pane -t team:0.1 -p`로 파인 출력 내용 읽기 (오케스트레이터가 서브에이전트 상태 모니터링에 활용)
- **TPM + tmux-resurrect**: 플러그인으로 세션 자동 복구 지원

---

## 6파인 팀 레이아웃

```
┌──────────────┬──────────────┬──────────────┐
│  Pane 0      │  Pane 1      │  Pane 2      │
│  오케스트레이터│  PM·아키텍트  │  리서처       │
├──────────────┼──────────────┼──────────────┤
│  Pane 3      │  Pane 4      │  Pane 5      │
│  디자이너     │  개발자       │  리뷰어       │
└──────────────┴──────────────┴──────────────┘
```

---

## 핵심 명령어

```bash
tmux new-session -s team          # 새 세션 생성
tmux ls                           # 세션 목록
tmux attach -t team               # 세션 접속
tmux send-keys -t team:0.1 "cmd" Enter  # 파인에 명령 전송
tmux capture-pane -t team:0.1 -p  # 파인 출력 캡처
tmux select-layout -t team tiled  # 격자 레이아웃
```

---

## 관련 노트

- [[Multi-Agent-System]] — TMUX로 구현하는 에이전트 팀 아키텍처
- [[Agentic-AI]] — TMUX가 Layer 2 역할을 담당
- [[Tools/Claude-Code]] — 각 파인에서 실행되는 에이전트 도구

---

## 출처

- `2.Areas/AgenticAI/claude_multiagent_guide.md` — Ch02~03 TMUX 설치·파인 레이아웃·셋업 스크립트
