# Emulate Write: a 100-prompt evaluation

**[Browse all 100 examples](https://dalek2point3.github.io/emulate-write-evaluation/)** · **[Download the research package](https://dalek2point3.github.io/emulate-write-evaluation/emulate-write-evaluation.zip)** · **[LaTeX paper](paper/emulate-paper.tex)**

An exploratory evaluation of Emulate's prompt-to-text Write workflow, conducted September 29, 2026. Author and writing-quality reviewer: **Codex**.

One unedited output was retained for each of 100 fixed English prompts across ten categories. All outputs were checked with Pangram 4 after their writing reviews were recorded.

| Pangram label | Documents |
|---|---:|
| Human | 85 |
| Mixed | 7 |
| AI | 8 |

**Every output is AI-generated.** Human is a detector classification, not a claim about provenance or writing quality. The Human-label share is 85% (descriptive Wilson 95% interval: 76.7–90.7%).

Writing ratings averaged 4.09/5 for adherence, 3.44/5 for coherence/readability, and 3.54/5 for development/usefulness. Thirteen outputs received coherence ratings of 1 or 2, and 70 met a ±20% word-count tolerance. These are subjective ratings from one AI assistant, not an independent human panel.

## Explore the evidence

- [Interactive report](https://dalek2point3.github.io/emulate-write-evaluation/): search prompts, outputs, and reviews; filter by category.
- [Complete joined results](data/evaluation.json): metadata and all 100 examples.
- [One example per line](data/examples.jsonl): JSONL for analysis.
- [Prompts](data/prompts.json), [review notes](data/review_notes.tsv), and [summary](data/summary.json).
- [Data dictionary](data/README.md) and [prompt/output hashes](data/text_hashes.json).
- [Prospective protocol](method/protocol.md), [targeted factual checks](method/factual_review.md), and [full report](paper/full-report.md).
- [Scientific paper in LaTeX](paper/emulate-paper.tex), with Codex as author.

## Reproduce the descriptive results

Python 3, standard library only:

```sh
python3 analysis/verify_results.py
```

This checks all 100 prompt and output hashes and recomputes labels, word counts, length compliance, average ratings, and the Human-label interval. It does not call either service or incur charges. New generations need not reproduce the original outputs.

The public package retains exact prompts, output text, per-document detector labels and fractions, version identifiers, request latency, charged words, and reviews. Raw account-access checks, credentials, internal service job IDs, and temporary files are excluded. The original private workspace retains raw service responses. Public hash checks verify consistency of the released text; they do not independently authenticate service provenance.

## Scope and limitations

This tests the complete Write workflow, including its internal rewriting stage. No existing draft was supplied for revision. There were no retries, exclusions, or detector-guided selections. Requested lengths were 150, 200, 300, and 500 words.

The prompts are a convenience sample, with ten observations per broad category and one per subcategory. There is no comparison generator, human control, or repeated sampling. The study cannot establish comparative superiority, overall detector accuracy, or a false-positive rate on human writing. The confidence interval is descriptive and does not address prompt-selection bias. Factual checks were targeted, not exhaustive.

This repository is not an official publication of Emulate or Pangram. Product and detector behavior may change after the evaluation date.

## Citation

```bibtex
@misc{codex2026emulate,
  author = {{Codex}},
  title = {Writing Quality and AI-Detector Labels in Emulate Write:
           A 100-Prompt Exploratory Evaluation},
  year = {2026},
  month = sep,
  url = {https://github.com/dalek2point3/emulate-write-evaluation},
  note = {Exploratory evaluation; one AI assistant reviewer}
}
```

Please cite the commit hash for the version analyzed. No additional reuse license is specified at present; public availability should not be interpreted as a blanket rights grant over service-generated text.

## Corrections

Open a GitHub issue with the example ID (W001–W100), the disputed claim or rating, and supporting evidence. Reviews are subjective and open to reassessment; the original outputs remain unchanged.
