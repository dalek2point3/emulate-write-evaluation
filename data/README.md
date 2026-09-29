# Data dictionary

`evaluation.json` contains `summary` (aggregate statistics) and `examples` (200 records). `examples.jsonl` contains the same example records, one per line. UTF-8 text is used throughout. Original whitespace is preserved in each `text` field.

| Field | Meaning |
|---|---|
| `id` | Stable example ID, W001–W200 |
| `round` | Generation round, 1 or 2; round 2 is an adaptive extension |
| `category`, `subcategory` | Broad category and distinct task type |
| `prompt` | Exact instruction submitted to Emulate |
| `requested_words` | Requested word count |
| `generation_status` | Generation completion state; all `success` |
| `text` | Exact Emulate output, unedited |
| `output_words` | Whitespace-separated words, including headings |
| `elapsed_seconds` | Observed generation-request duration |
| `charged_words` | Emulate-reported charged words |
| `detection_status` | Detector completion state; all `success` |
| `label` | Exact Pangram document label: Human, Mixed, or AI |
| `fraction_ai`, `fraction_ai_assisted`, `fraction_human` | Pangram-estimated portions of text, not provenance probabilities |
| `detector_version` | Returned detector version, `4.0` |
| `review` | ID; adherence, coherence, development ratings; concrete notes |
| `word_ratio` | Observed / requested words |
| `within_20_percent` | Whether observed length is within ±20% of request |

Rating values are stored as strings in the original joined data; convert to integers for analysis. The scale is 1 (fails), 2 (major weakness), 3 (noticeable weakness), 4 (minor weakness), 5 (fully meets criterion). All ratings came from one AI assistant reviewer before detector results were inspected.

`prompts.json` uses `words` for the requested length and contains a SHA-256 prompt hash. `review_notes.tsv` is the preserved review table. `text_hashes.json` separately records SHA-256 hashes of the UTF-8 prompt and output text for each example.

The summary contains pooled statistics plus `rounds` and `categories` breakdowns. Means use decimal half-up rounding to two places. Intervals and means describe this convenience sample only; they do not correct for adaptive prompting or reviewer dependence. Auxiliary detector flags and billing estimates are not included in this release's summary. The original 100-text release remains available under the `v1-100-texts` tag.
