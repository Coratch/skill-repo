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

### McKinsey Analysis

`mckinsey-analysis` is a McKinsey-style consulting analysis skill for complex decisions, project diagnosis, strategy, product planning, organization issues, technical reviews, MECE decomposition, evidence-backed executive summaries, slide/storyline design, and action plans.

It is designed to help turn ambiguous problems into decision-ready analysis:

- define the real issue and decision context
- decompose problems with MECE issue trees
- form and test hypotheses with WWHTBT
- apply 80/20 prioritization and So What reasoning
- separate facts, estimates, inferences, and assumptions
- design executive storylines and dummy pages for PPT-style deliverables
- synthesize conclusions with pyramid structure
- produce prioritized action plans and pressure tests

### Architecture Review

`architecture-review` is a general architecture review skill for technical design reviews, ADR critique, runtime flow analysis, data contract review, migration review, failure mode analysis, and adversarial review.

It is designed to make architecture decisions evidence-first and reviewable:

- define review scope, non-goals, constraints, and success criteria
- map runtime nodes, responsibilities, input/output objects, persistence, and downstream consumers
- identify existing capabilities and avoid unnecessary rebuilds
- review contracts for stability, validation, compatibility, and observability
- distinguish natural language output from system-consumable structured contracts
- compare current, minimal-change, long-term, and do-nothing options
- challenge the preferred design with applicability boundaries and failure modes

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
├── mckinsey-analysis/
│   ├── SKILL.md
│   └── test-prompts.json
├── architecture-review/
│   ├── SKILL.md
│   └── references/
│       ├── failure-modes.md
│       ├── output-templates.md
│       └── review-checklist.md
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
Use $mckinsey-analysis to analyze this product strategy.
```

```text
Use $mckinsey-analysis to create a MECE issue tree and action plan for this project risk.
```

```text
Use $mckinsey-analysis to turn this messy problem into an executive summary.
```

```text
Use $mckinsey-analysis to create a CEO storyline and dummy pages for this strategy review.
```

```text
Use $architecture-review to review this technical design and list failure modes.
```

```text
Use $architecture-review in contract-review mode to examine these input and output objects.
```

```text
Use $architecture-review to challenge this recommended architecture choice from a review-board perspective.
```

## Modes

### Article Learning Coach

| Mode | Purpose |
|---|---|
| `scan` | First-pass orientation with thesis, 5W2H, and core claims |
| `deep` | Full learning pass with SCQA, evidence, assumptions, critique, and transfer |
| `coach` | Interactive Feynman-style explanation and gap diagnosis |
| `memory` | Active-recall questions, flashcards, and spaced-review plan |

### McKinsey Analysis

| Mode | Purpose |
|---|---|
| Quick diagnostic | Fast judgment for reviews, decisions, product plans, and document critique |
| Full consulting | Complete issue definition, MECE decomposition, hypothesis testing, synthesis, action plan, and pressure test |
| Executive storyline | Storyline, dummy pages, chart/data needs, and slide-title style synthesis |

### Architecture Review

| Mode | Purpose |
|---|---|
| `proposal-review` | Review design docs, technical proposals, ADRs, and implementation plans |
| `runtime-flow-review` | Review end-to-end execution flow, states, persistence, and downstream consumers |
| `contract-review` | Review API, event, task, config, model-output, and data contracts |
| `incident-architecture-review` | Derive architecture-level root cause from failures and integration logs |
| `migration-review` | Review compatibility, rollout, rollback, and migration paths |
| `adversarial-review` | Challenge the preferred design and list boundaries and failure modes |

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
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py mckinsey-analysis
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py architecture-review
```

Check the PDF extraction script syntax:

```bash
python -m py_compile article-learning-coach/scripts/extract_pdf_text.py
```
