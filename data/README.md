# Data dictionary

`evaluation.json` contains `summary` (aggregate statistics) and `examples` (100 records). `examples.jsonl` contains the same example records, one per line. UTF-8 text is used throughout. Original whitespace is preserved in each `text` field.

| Field | Meaning |
|---|---|
| `id` | Stable example ID, W001–W100 |
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

Summary category intervals and means describe this sample only. The estimated Pangram bulk charge in the summary is a calculation from word counts and the published rate, not an invoice. The six documents with an auxiliary humanizer flag are represented in the aggregate summary; raw window-level flags are not included in this curated release.
