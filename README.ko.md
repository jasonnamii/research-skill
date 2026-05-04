# 리서치 스킬

> 🇺🇸 [English README](./README.md)

**체계적 리서치 엔진 — WHY · HOW · SCOPE + BLIND · EXPAND, 7층 사고 중첩.**

## 사전 요구사항

- **Claude Cowork 또는 Claude Code** 환경
- **웹 검색 접근** — DEEP 모드 권장
- **trigger-dictionary** 스킬 (필수, 선행 로드)

## 목적

구조 없는 리서치는 시간을 낭비하거나 핵심을 놓친다. `research-skill`은 3축 방법론(WHY · HOW · SCOPE)에 7층 사고(L0 제1원리 → L7 오컴)를 중첩하고, 4모드(LIGHT · DEEP · TURBO · EXPAND)와 v2.7 증거 무결성(EVIDENCE_BODY · SOURCE_CONTRAST · CLAIM_PROVENANCE)을 강제한다.

## 모드

| 모드 | 트리거 | 용도 |
|------|--------|------|
| LIGHT | "라이트" | 폭 스캔, 확신도 cap 50 |
| DEEP | 기본 | 풀 조사, 5장르 매트릭스, 8대 의무 |
| TURBO | "터보" | 축 병렬 발행 |
| EXPAND | "확장" | 프레임 밖 탐색 (예산제) |

## 증거 무결성 (v2.7)

"표·등급만 있고 본문에 원자료 휘발" 실패 패턴을 차단하는 8대 의무:

- **B1 양적 포화** — 깊이별 1차 인용 N (≥15·8·3)
- **B2 출처 차수** — 1차/2차/3차 라벨
- **B3 정량 불확실성** — (N=?, K=?, 시점=?)
- **B4 반증 대칭** — 지지:반증 1:1
- **B5 시간성** — (YYYY-MM, 맥락)
- **S1 EVIDENCE_BODY** — 결론 한 줄당 1차 출처 1+ 본문 인용
- **S2 SOURCE_CONTRAST** — DEEP 5장르 대비표 의무
- **S3 CLAIM_PROVENANCE** — 모든 평가 옆 근거ID 명시

## 산출물 구조

| 유형 | 경로 |
|------|------|
| DEEP | `_research/[축].md` |
| LIGHT | `_research/LIGHT_[축].md` |
| EXPAND | `_research/EXPAND_[T]_[축].md` |

템플릿: `references/output-template.md`

## 계보

[research-frame](https://github.com/jasonnamii/research-frame)에서 v3.0 (2026-05-04) 리네임. 토큰 다이어트로 SKILL.md 47% 압축, 모든 룰·의무는 `references/`에 박제하여 손실 ZERO.

## 라이선스

MIT
