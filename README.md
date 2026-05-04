# research-skill

> 🇰🇷 [한국어 README](./README.ko.md)

**Systematic research engine — WHY · HOW · SCOPE + BLIND · EXPAND, layered with 7-tier thinking.**

## Prerequisites

- **Claude Cowork or Claude Code** environment
- **Web search access** — recommended for DEEP mode
- **trigger-dictionary** skill (required, loaded ahead)

## Goal

Research without structure wastes time on irrelevant details or misses critical findings. `research-skill` provides a three-axis methodology (WHY · HOW · SCOPE) layered with 7-tier thinking (L0 first-principles → L7 Occam), 4 modes (LIGHT · DEEP · TURBO · EXPAND), and v2.7 evidence integrity (EVIDENCE_BODY · SOURCE_CONTRAST · CLAIM_PROVENANCE).

## Modes

| Mode | Trigger | Use case |
|------|---------|----------|
| LIGHT | "라이트" | Breadth scan, confidence cap 50 |
| DEEP | default | Full investigation, 5-genre matrix, 8 mandatory rules |
| TURBO | "터보" | Parallel axis dispatch |
| EXPAND | "확장" | Frame-external exploration with budget cap |

## Evidence integrity (v2.7)

8 mandatory rules to prevent the "table-and-rating without body citation" failure mode:

- **B1 Quantitative saturation** — depth-based 1st-source N (≥15·8·3)
- **B2 Source tier label** — 1st/2nd/3rd
- **B3 Numeric uncertainty** — (N=?, K=?, time=?)
- **B4 Counter-evidence symmetry** — 1:1 support:rebuttal
- **B5 Temporal stamp** — (YYYY-MM, context)
- **S1 EVIDENCE_BODY** — every conclusion line cites a 1st source in body
- **S2 SOURCE_CONTRAST** — DEEP requires 5-genre comparison table
- **S3 CLAIM_PROVENANCE** — every rating links to fact-ledger row ID

## Output structure

| Type | Path |
|------|------|
| DEEP | `_research/[axis].md` |
| LIGHT | `_research/LIGHT_[axis].md` |
| EXPAND | `_research/EXPAND_[T]_[axis].md` |

Templates: `references/output-template.md`

## Heritage

Renamed from [research-frame](https://github.com/jasonnamii/research-frame) at v3.0 (2026-05-04) with token diet — SKILL.md 47% smaller while preserving every rule and mandate via `references/`.

## License

MIT
