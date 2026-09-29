# Emulate Write: a 200-prompt, two-round evaluation

**[Browse all 200 examples](https://dalek2point3.github.io/emulate-write-evaluation/)** · **[Download the research package](https://dalek2point3.github.io/emulate-write-evaluation/emulate-write-evaluation.zip)** · **[Read the PDF](docs/emulate-paper.pdf)** · **[LaTeX source](paper/emulate-paper.tex)**

An exploratory evaluation of Emulate's prompt-to-text Write workflow, conducted September 29, 2026. Author and writing-quality reviewer: **Codex**.

One unedited output was retained for each of 200 English prompts, fixed before generation within each round, across ten categories. Each round was checked with Pangram 4 after its writing reviews were recorded. Round 2 is an adaptive extension: new scenarios and some more explicit constraints were informed by round-1 findings.

| Pangram label | Round 1 | Round 2 | Pooled |
|---|---:|---:|---:|
| Human | 85 | 81 | 166 |
| Mixed | 7 | 2 | 9 |
| AI | 8 | 17 | 25 |

**Every output is AI-generated.** Human is a detector classification, not a claim about provenance or writing quality. The Human-label share is 83% (descriptive Wilson 95% interval: 77.2–87.6%).

Writing ratings averaged 4.06/5 for adherence, 3.49/5 for coherence/readability, and 3.52/5 for development/usefulness. Twenty-one outputs received coherence ratings of 1 or 2, and 132 (66%) met a ±20% word-count tolerance. These are subjective ratings from one AI assistant, not an independent human panel.

## Explore the evidence

- [Interactive report](https://dalek2point3.github.io/emulate-write-evaluation/): search prompts, outputs, and reviews; filter by category, round, and detector label.
- [Complete joined results](data/evaluation.json): metadata and all 200 examples.
- [One example per line](data/examples.jsonl): JSONL for analysis.
- [Prompts](data/prompts.json), [review notes](data/review_notes.tsv), and [summary](data/summary.json).
- [Data dictionary](data/README.md) and [prompt/output hashes](data/text_hashes.json).
- [Prospective protocol](method/protocol.md), [targeted factual checks](method/factual_review.md), and [full report](paper/full-report.md).
- [Scientific paper (PDF)](docs/emulate-paper.pdf).
- [Scientific paper in LaTeX](paper/emulate-paper.tex), with Codex as author.

Round 2 has a separate [protocol addendum](method/round2-protocol.md) and [factual review](method/round2-factual-review.md). The original 100-text release is preserved at [v1-100-texts](https://github.com/dalek2point3/emulate-write-evaluation/tree/v1-100-texts). Between-round differences are descriptive, not causal estimates.

## Reproduce the descriptive results

Python 3, standard library only:

```sh
python3 analysis/verify_results.py
```

This checks all 200 prompt and output hashes and recomputes labels, word counts, length compliance, average ratings, and the Human-label interval. It does not call either service or incur charges. New generations need not reproduce the original outputs.

The public package retains exact prompts, output text, per-document detector labels and fractions, version identifiers, request latency, charged words, and reviews. Raw account-access checks, credentials, internal service job IDs, and temporary files are excluded. The original private workspace retains raw service responses. Public hash checks verify consistency of the released text; they do not independently authenticate service provenance.

## Scope and limitations

This tests the complete Write workflow, including its internal rewriting stage. No existing draft was supplied for revision. All generations succeeded on their first attempt, with no exclusions or detector-guided selections. Round 2 required an administrative detector-submission retry after an insufficient-credit rejection; the saved outputs were unchanged. Requested lengths were 150, 200, 300, and 500 words.

The prompts are a convenience sample, with 20 observations per broad category and two per task type. There is no comparison generator, human control, or repeated sampling. The study cannot establish comparative superiority, overall detector accuracy, or a false-positive rate on human writing. The confidence interval is descriptive and does not address prompt-selection bias. Factual checks were targeted, not exhaustive.

This repository is not an official publication of Emulate or Pangram. Product and detector behavior may change after the evaluation date.

## Citation

```bibtex
@misc{codex2026emulate,
  author = {{Codex}},
  title = {Writing Quality and AI-Detector Labels in Emulate Write:
           A 200-Prompt, Two-Round Exploratory Evaluation},
  year = {2026},
  month = sep,
  url = {https://github.com/dalek2point3/emulate-write-evaluation},
  note = {Exploratory evaluation; one AI assistant reviewer}
}
```

Please cite the commit hash for the version analyzed. No additional reuse license is specified at present; public availability should not be interpreted as a blanket rights grant over service-generated text.

## Corrections

Open a GitHub issue with the example ID (W001–W200), the disputed claim or rating, and supporting evidence. Reviews are subjective and open to reassessment; the original outputs remain unchanged.
