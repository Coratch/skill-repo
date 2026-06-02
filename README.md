# Skill Repo

Personal agent skills for structured learning and knowledge work.

## Skills

### Article Learning Coach

`article-learning-coach` is a learning coach for professional articles, research papers, technical blogs, reports, PDFs, URLs, DOIs, and pasted text.

It is designed to move beyond generic summarization. The workflow helps a learner:

- identify the article's central thesis
- map the article with 5W2H
- reconstruct the argument with SCQA
- analyze claims, evidence, warrants, assumptions, and limitations
- explain difficult concepts in plain and technical language
- use a Feynman loop to test understanding
- create active-recall questions, memory cards, and spaced-review prompts

### McKinsey

`mckinsey` is a structured consulting analysis skill for complex decisions, project diagnosis, strategy, product planning, organization issues, technical reviews, MECE decomposition, hypothesis-driven analysis, executive summaries, and action plans.

It is designed to help turn ambiguous problems into decision-ready analysis:

- define the real issue and decision context
- decompose problems with MECE issue trees
- form and test hypotheses with WWHTBT
- apply 80/20 prioritization and So What reasoning
- synthesize conclusions with pyramid structure
- produce prioritized action plans and pressure tests

## Repository Structure

```text
skill-repo/
├── README.md
├── article-learning-coach/
│   ├── SKILL.md
│   ├── agents/
│   │   └── openai.yaml
│   ├── references/
│   │   ├── article-types.md
│   │   ├── methods.md
│   │   └── output-templates.md
│   └── scripts/
│       └── extract_pdf_text.py
├── mckinsey/
│   └── SKILL.md
└── .gitignore
```

## Usage Examples

```text
Use $article-learning-coach to help me deeply learn this PDF.
```

```text
Use $article-learning-coach in scan mode for this article URL.
```

```text
Use $article-learning-coach in coach mode. Ask me to explain the article, then diagnose my understanding gaps.
```

```text
Use $article-learning-coach in memory mode and generate Anki-style cards.
```

```text
Use $mckinsey to analyze this product strategy.
```

```text
Use $mckinsey to create a MECE issue tree and action plan for this project risk.
```

```text
Use $mckinsey to turn this messy problem into an executive summary.
```

## Modes

### Article Learning Coach

| Mode | Purpose |
|---|---|
| `scan` | First-pass orientation with thesis, 5W2H, and core claims |
| `deep` | Full learning pass with SCQA, evidence, assumptions, critique, and transfer |
| `coach` | Interactive Feynman-style explanation and gap diagnosis |
| `memory` | Active-recall questions, flashcards, and spaced-review plan |

### McKinsey

| Mode | Purpose |
|---|---|
| Quick diagnostic | Fast judgment for reviews, decisions, product plans, and document critique |
| Full consulting | Complete issue definition, MECE decomposition, hypothesis testing, synthesis, action plan, and pressure test |

## PDF Text Extraction

For local PDFs, the article learning skill includes a small helper script:

```bash
python article-learning-coach/scripts/extract_pdf_text.py input.pdf --output article.txt
```

The script tries `pypdf` first, then falls back to the `pdftotext` CLI if available.

## Validation

Validate the skills with the Codex skill creator validator:

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py article-learning-coach
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py mckinsey
```

Check the PDF extraction script syntax:

```bash
python -m py_compile article-learning-coach/scripts/extract_pdf_text.py
```
