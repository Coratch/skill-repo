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

## Modes

| Mode | Purpose |
|---|---|
| `scan` | First-pass orientation with thesis, 5W2H, and core claims |
| `deep` | Full learning pass with SCQA, evidence, assumptions, critique, and transfer |
| `coach` | Interactive Feynman-style explanation and gap diagnosis |
| `memory` | Active-recall questions, flashcards, and spaced-review plan |

## PDF Text Extraction

For local PDFs, the skill includes a small helper script:

```bash
python article-learning-coach/scripts/extract_pdf_text.py input.pdf --output article.txt
```

The script tries `pypdf` first, then falls back to the `pdftotext` CLI if available.

## Validation

Validate the skill with the Codex skill creator validator:

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py article-learning-coach
```

Check the PDF extraction script syntax:

```bash
python -m py_compile article-learning-coach/scripts/extract_pdf_text.py
```
