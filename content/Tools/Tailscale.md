---
wiki_type: entity
tags: [wiki, tools, tailscale, vpn, remote-access, wireguard]
sources:
  - "[[../../1.Projects/Raingent/Migration/원격 접속 설정]]"
updated: 2026-05-31
---

# Tailscale

WireGuard 암호화 기반 Mesh VPN 서비스. 방화벽·NAT 뒤에 있는 기기들을 포트 포워딩 없이 안전하게 연결한다. Raingent에서는 MacBook ↔ Ubuntu PC 원격 접속에 사용.

---

## 핵심 내용

- **동작 원리**: Control Server(키 교환) → STUN/P2P 직접 연결 → DERP 서버 중계(fallback) 순서
- **기기마다 고정 IP**: `100.x.x.x` Tailscale IP 자동 부여 (유동 공인 IP 무관)
- **인증**: Google/GitHub SSO + 2FA 지원, SSH 키 관리 불필요
- **Tailscale SSH**: `sudo tailscale set --ssh` 활성화 시 키 없이 SSH 접속 가능
- **MagicDNS**: 관리 콘솔 DNS 탭에서 활성화 시 IP 대신 호스트명으로 접속 가능

## Raingent 기기 정보

| 기기 | 호스트명 | Tailscale IP |
|------|----------|--------------|
| Ubuntu PC | `rainny-ubuntu-24` | 100.122.69.43 |
| MacBook Pro | `griffy-macbook-pro` | 100.124.68.115 |

- **계정**: eldanscript@gmail.com
- **관리 콘솔**: https://login.tailscale.com/admin/machines

## 접속 명령어

```bash
# SSH 접속
tailscale ssh rainny@rainny-ubuntu-24

# VNC 화면 공유 (MacBook Finder에서)
open vnc://100.122.69.43:5900
```

## VNC 서비스 (Ubuntu)

- 서비스: `x11vnc.service` (`/etc/systemd/system/x11vnc.service`)
- 포트: 5900
- 재시작: `sudo systemctl restart x11vnc.service`

---

## 관련 노트

- [[../Projects/Raingent]]
