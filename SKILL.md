---
name: research-skill
description: "발동 트리거 2개만: '딥리서치' 또는 '확장리서치'. 그 외 단어(리서치·조사·research 등 일반어)로는 발동 ✗. DEEP·EXPAND 모드 7층 사고 리서치 엔진(WHY·HOW·SCOPE + BLIND + EXPAND). 본격 다축 조사·가설검증·1차출처 인용·반증대칭. NOT: 정책기획(→policy-planning), 단순팩트체크(→fact-checker)."
version: 3.1
---

# Research Skill — WHY·HOW·SCOPE + 7층 사고

🔗 **REQUIRES:** `trigger-dictionary` (선행 로드) — §1~§5 전구간 정식명 발동. INV 9.


## Skill Boundaries

- **하는 것** — "발동 트리거 2개만: '딥리서치' 또는 '확장리서치'.
- **안 하는 것** — 정책기획(→policy-planning), 단순팩트체크(→fact-checker)."

리서치 "왜·어떻게·어디까지" 구조화. UP §E 위에 7층(L0 제1원리·L1 장르·L2 홈즈·L3 삼각·L4 연역수렴·L5 아날로지·L6 맥가이버·L7 오컴) 중첩.

**발동:** 다축·가설검증·교차분석 (단순 팩트체크는 UP §E)
**🛡️ INV·PREFLIGHT·RESET·STEALTH·FINAL_RENDER_GATE·v2.7 의무 8종(B1~B5·S1~S3):** → `references/invariants.md`

---

## When to Use

- 사용자가 P2 트리거 동사구 같은 표현으로 발동
- 도메인 작업이 필요한 시점
- **안 쓸 때** — 정책기획(→policy-planning), 단순팩트체크(→fact-checker)."


## Prerequisites

| # | 체크 | 미충족 시 |
|---|------|-----------|
| 1 | 대상·입력 명확 (스킬 발동 의도 확인) | 1줄 확인 후 진입 |
| 2 | references/ 폴더 접근 가능 | inline fallback |
| 3 | scripts/ 실행 권한 | 권한 보정 후 재시도 |


## 모드

진입: 🎯 작업설계자 → 트리아지 → 모드

| | LIGHT | DEEP | TURBO | EXPAND |
|---|---|---|---|---|
| 트리거 | "라이트" | 기본 | "터보" | "확장" |
| 확신도 | 50 cap | 판정표 | DEEP | DEEP |
| BLIND | S1·S3 | S1·S2·S3 | DEEP+병렬 | DEEP+T |
| 산출 | LIGHT_[축].md | [축].md | DEEP | EXPAND_*.md |
| **B1 N** | 3 고정 | 전수15·표본8·스캔3 | DEEP | DEEP |
| **B4 1:1** | 면제(1회) | 강제 | DEEP | DEEP |

LIGHT→DEEP: rename. **흐름:** §1 WHY → 게이트 → §2 HOW → 게이트 → §3 SCOPE ↳§4 BLIND → §5 EXPAND → 편입

**원칙:** 중복 회계 제거 · FIG 3블록 · 예산제 · 객관 메트릭 복귀 · 정식명 본문 노출(INV 9) · **본문 인용(INV 10)**

| references/ | 역할 |
|---|---|
| `why.md`·`how.md`·`scope.md` | §1·§2·§3 본문 |
| `blind.md`·`expand.md` | §4·§5 본문 |
| `invariants.md` | INV 12 + v2.7 의무 8종 + FINAL_RENDER_GATE + Self-Check |
| `output-template.md` | DEEP·LIGHT 산출 템플릿 (피라미드 원칙 + PRISMA 투명성) |
| `rationale.md`·`turbo.md`·`gotchas-extended.md` | 근거·병렬·함정 |

---

## §1·§2·§3·§4·§5 요약

→ `why.md`·`how.md`·`scope.md`·`blind.md`·`expand.md`

- **§1 WHY:** 1-1 결정연결 **제1원리·백본** · 1-2 가설+경쟁3+ **백본** · 1-3 MECE·전제 **틀밖·절대자** → 게이트
- **§2 HOW:** 2-1 축별 병렬·5장르·FIG·**B1·B2·B5** **홈즈·엄브렐러·프리모르템** · 2-2 반대증거 허브·**B4 1:1** · 2-3 ACH·**S2 5장르대비표** **연역수렴·오컴** · 2-4 회귀 **수정4** → 게이트
- **§3 SCOPE:** 3-1 경계 · 3-2 한계 **맥가이버** · 3-3 깊이 **트리아지** · 3-4 종료 **스켈레톤·제출청소** · 3-5 신뢰도·**B3 정량메타** **오컴** · LIGHT cap 50
- **§4 BLIND:** S1 비대칭 · S2 부재 · S3 반증공백. 자기고발=+1 보너스, 숨김=2tier↓
- **§5 EXPAND:** 예산=축×0.5(상한3). T1·T2·T3. 복귀=객관 메트릭. **타임스톤** 4항

---

## §6 트리거 (v2.6)

7층×정식명×주입. **본문 노출 필수** (HARD-FIRE, STEALTH 면제).

| 층 | 정식명 | 주입 |
|---|---|---|
| L0 | 제1원리·백본·작업설계자·트리아지 | §1-1·모드 |
| L1 | 엄브렐러·프리모르템 | §2-1 장르 |
| L2 | 홈즈 | §2-1·§4 |
| L3 | (수렴4축·FIG 내재) | §2 |
| L4 | 연역수렴·오컴·외과적·수정4 | §2-3·§2-4 |
| L5 | 아날로지·줌 | §5 T2·T3 |
| L6 | 맥가이버·틀밖·절대자 | §3-2·§1-3·§5 T1 |
| L7 | 오컴·외과적 | §3-5·FIG |
| 종료 | 스켈레톤·제출청소·타임스톤 | §3-4·§5 |

---

## 산출물

| 유형 | 경로 |
|---|---|
| DEEP | `_research/[축].md` (맹점+**본문인용+5장르대비+근거ID**) |
| LIGHT | `_research/LIGHT_[축].md` |
| EXPAND | `_research/EXPAND_[T]_[축].md` |

**템플릿 전문 (DEEP·LIGHT·경량화 상한):** → `references/output-template.md`

---

## Reference Index

| 파일 | 내용 | 언제 |
|---|---|---|
| `references/blind.md` | blind | 해당 단계 진입 시 |
| `references/expand.md` | expand | 해당 단계 진입 시 |
| `references/gotchas-extended.md` | gotchas extended | 해당 단계 진입 시 |
| `references/how.md` | how | 해당 단계 진입 시 |
| `references/invariants.md` | invariants | 해당 단계 진입 시 |
| `references/output-template.md` | output template | 해당 단계 진입 시 |
| `references/rationale.md` | rationale | 해당 단계 진입 시 |
| `references/scope.md` | scope | 해당 단계 진입 시 |
| `references/turbo.md` | turbo | 해당 단계 진입 시 |
| `references/why.md` | why | 해당 단계 진입 시 |

## Next Phase

본 스킬 작업 후 자연스럽게 이어지는 흐름:

- 후속 작업 → `policy-planning`
- 후속 작업 → `fact-checker`

## Output Path

| 산출물 | 경로 |
|---|---|
| 주 산출물 | `mnt/outputs/research-skill\_{topic}_{YYYY-MM-DD}.md` |
| 리서치 결과 (해당 시) | `{VAULT}/_skills research/research-skill/{YYYY-MM-DD}_{topic}.md` |

## Failure Modes (Gotchas) (Top 10)

1. 중복 회계 → 단일 지점
2. WHY 게이트 스킵 → 3개 채움
3. 축 오염 → 병렬 발행
4. LIGHT cap 초과 → 50 절삭
5. FIG 미가동 → 수집+결론 필수
6. 트리거 정식명 누락 → §6 노출(INV 9)
7. EXPAND 자의 연장 → 객관 메트릭
8. **본문 원자료 미인용** → INV 10·EVIDENCE_BODY FAIL
9. **5장르 후 단일장르 결론** → INV 11·SOURCE_CONTRAST FAIL
10. **별점 옆 근거ID 누락** → INV 12·CLAIM_PROVENANCE FAIL

❌ WRONG: 표·등급만 적층, 본문에 원자료 휘발 (양평 종합 패턴)
✅ CORRECT: 결론 한 줄당 1차 출처 1+ 본문 인용 (INV 10·S1)

→ `gotchas-extended.md`·`invariants.md`·`CHANGELOG.md`
