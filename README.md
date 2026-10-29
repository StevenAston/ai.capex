# The AI Standoff: Who pays for progress?

A working research narrative connecting AI capital expenditure, implementation costs, household-financed computerization, practical expertise and the incentives for worker cooperation.

## Read

Open [index.html](index.html) in a browser. It is self-contained and requires no installation or server.

- 16 chapters and 64 propositions, with 16 explanatory diagrams.
- Narrative and point-form reading modes, search and an assumptions calculator.
- [Complete point-form narrative](ai_standoff_outline.md).
- [Reconciled Shadow Capital paper](the_shadow_capital_of_the_digital_revolution.md).
- [Annual model data](shadow_capital_annual.csv).
- [Standalone model and inputs](shadow_capital_model.zip).

The source ledger distinguishes project arguments, empirical evidence and modelling assumptions.

## Reproduce

Requires Python 3.9 or later; the build and model use the standard library.

    python build.py
    python research/shadow_capital_model.py --output scenario.csv

Edit the narrative in sites/shadow-capital-narrative/content.json. The build generates the reading page and outline from this common source. CSS, browser interactions and page generation live beside it.

Optional interaction checks require Node.js:

    cd sites/shadow-capital-narrative
    node verify-controls.cjs

## Model status

The reconciled baseline uses the exported paper's annual arrays for the United States, 1980–2010, in cumulative nominal USD:

| Measure | Baseline |
| --- | ---: |
| Corporate IT expenditure | $9.852 trillion |
| Career-attributed household expenditure | $707.20 billion |
| Imputed unpaid learning time | $1.90449 trillion |
| Combined gross household cost | $2.61169 trillion |
| Combined/corporate expenditure | 26.51% |

Baseline assumptions: 40% career attribution, 1.5 learning hours per week, 52 weeks per year and a 75% shadow-wage factor. Ancillary expenditure is included subject to an overlap audit. The unexplained 1.815 multiplier was removed.

**Arithmetic reconciliation is not source validation.** The historical input arrays and attribution parameters are provisional. Gross household cost is not an identified net uncompensated transfer. The original exported draft is retained in research/shadow_capital_exported_draft.md for comparison.

## Verification

The local checks covered model totals, ancillary exclusion, zero-input behaviour, annual/period reconciliation, local links and anchors, search, reading mode and calculator behaviour. Visual browser inspection and hosted deployment were unavailable in the authoring session.

This repository contains no deployment credentials or connection metadata. No license has been selected.
