---
wiki_type: entity
tags: [wiki, company, furiosaai, npu, ai-chip, semiconductor, korea]
sources:
  - 2.Areas/FuriosaAI/Summit 2026/(406) RENEGADE 2026_ RNGD Mass Production, Performance Benchmarks, Enterprise Deployment, Cloud Partners - YouTube - Detailed report.md
updated: 2026-05-31
---

# FuriosaAI

한국의 AI 반도체 스타트업. **AI 컴퓨팅의 에너지 효율성을 극대화**하는 NPU(신경처리장치)를 개발·양산하며, 누구나 강력한 AI를 경제적으로 사용할 수 있는 생태계 구축을 목표로 한다.

---

## 핵심 내용

- **설립 배경**: 알파고 쇼크 이후 AI 컴퓨팅 초기 단계(약 9년 전)부터 AI 전용 반도체 개발에 착수, AI 컴퓨팅 비용 절감을 핵심 사명으로 삼는다
- **주력 제품**: RNGD(RENEGADE) — 200W TDP 제약 내에서 512 TFLOPS(FP16 AP) 달성, HBM3 메모리, 400억 트랜지스터 집적
- **TCP 아키텍처**: Tensor Contract Processor — 효율성·범용성·생산준비성 세 축으로 설계. 데이터 이동을 최소화해 GPU 대비 에너지 효율 우수
- **양산 현황**: 2021년 설계 착수 → 2024년 샘플 출시 → 2025년 1월 양산 시작. 2025년 약 2만 개 RENEGADE 카드 공급
- **성능 비교**: NVIDIA RTX Pro 6000(600W)과 동등 처리량을 180W TDP로 달성 — 와트당 처리량 약 3배 우위
- **생태계 파트너**: TSMC(파운드리), SK하이닉스(HBM3), Supermicro(서버 어플라이언스), LG AI·LG U+, 삼성 SDS, Upstage, 메가존 클라우드

---

## RENGADE(RNGD) 칩 상세

| 항목 | 사양 |
|------|------|
| 아키텍처 | TCP (Tensor Contract Processor) |
| 연산 성능 | 512 TFLOPS (FP16 AP) |
| 트랜지스터 | 400억 개 |
| 메모리 | HBM3 (4세대), 2.5D 인터포저 패키징 |
| TDP | 200W 이하 (실측 180W) |
| 서버 어플라이언스 | 8카드 탑재, 3kW 전력, ~4 PetaFLOPS, 384GB 메모리 |

### 소프트웨어 스택

- PyTorch 모델 → 자체 컴파일러 → 최적화 바이너리 → 서빙 시스템
- OpenAI API 호환, Kubernetes(DRA/LMD) 지원, VLM 호환
- FP8, BF16, MX FP4, MVFP4 등 다양한 데이터 타입을 소프트웨어 업데이트만으로 지원

---

## RENEGADE 2026 Summit 발표 (2026-05-31)

- **양산 완료 선언**: 2025년 1월부터 양산. 현재 고객 공급 중
- **성능 벤치마크 공개**: X41.032B 모델 기준 배치 512, 처리량 12,000 토큰/초 달성
- **엔터프라이즈 배포 사례**: LG AI ExaOne 모델 최적화 완료, LG U+ B2C 서비스(콜 에이전트·IPTV) 적용
- **클라우드 파트너십**: 삼성 SDS — 2025년 7월 구독형 NPU-as-a-Service(Azure) 국내 최초 출시 예정
- **글로벌 확장**: 메가존 클라우드 주도 중동(사우디) 수출 프로젝트, 향후 5년간 약 3,000억 원 규모
- **로드맵**: RENEGADE S(PC/워크스테이션용) 2025년 말~2026년 초, 3세대 칩 2028년 예정

---

## 관련 노트

- [[NPU-AI-Chip-Landscape]] — FuriosaAI·NVIDIA 등 AI 칩 생태계 비교
- [[AWS-Summit-Seoul-2026]] — AWS Summit에서 Trainium 등 경쟁 칩 발표
- [[Agentic-AI]] — RENEGADE가 지원하는 에이전트 추론 워크로드
- [[Entities/Companies/AWS]] — 클라우드 파트너 및 경쟁 AI 칩(Trainium) 제조사

---

## 출처

- `2.Areas/FuriosaAI/Summit 2026/(406) RENEGADE 2026_ RNGD Mass Production, Performance Benchmarks, Enterprise Deployment, Cloud Partners - YouTube - Detailed report.md`
