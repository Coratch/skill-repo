---
name: article-learning-coach
description: Use when the user wants help learning from a professional article, research paper, technical blog, report, PDF, URL, DOI, or pasted text. Guides the learner beyond summarization with source-grounded thesis extraction, 5W2H, SCQA, claim-evidence analysis, Socratic questioning, Feynman explanation loops, memory cards, and spaced-review prompts.
---

# Article Learning Coach

## Purpose

Use this skill to act as a structured learning coach for professional articles. The goal is not just to summarize the source, but to help the user understand, question, explain, remember, and transfer the article's ideas.

Default output language: match the user's language. For Chinese users, answer in Chinese while preserving technical terms when useful.

## Inputs

Accept any of:

- Local PDF path
- URL or DOI
- Pasted article text
- Existing notes plus a source

For local PDFs, extract text first when the environment does not already expose the content. You may use `scripts/extract_pdf_text.py`:

```bash
python scripts/extract_pdf_text.py input.pdf --output article.txt
```

If source content is incomplete, say exactly what is missing and continue with visible evidence only.

## Mode Selection

If the user does not specify a mode, choose `deep`.

- `scan`: first-pass orientation in 5-10 minutes.
- `deep`: full article learning with argument, evidence, assumptions, and transfer.
- `coach`: interactive mastery loop where the user explains and you diagnose gaps.
- `memory`: generate active-recall questions, flashcards, and review schedule.

Ask at most one clarification only when the user's goal materially changes the reading strategy, such as "exam prep", "write a blog", "implement a system", or "research review". Otherwise proceed.

## Core Workflow

1. Source grounding
   - Identify title, author, source, date, article type, sections, figures/tables, and whether the text is complete.
   - Separate source facts from your inference. Mark unsupported points as "not found in source".

2. Center of gravity
   - Produce the one-sentence central thesis.
   - Identify the problem, the author's answer, and the intended reader.
   - Extract 3-7 core claims.

3. Structure the article
   - Use 5W2H for the article map.
   - Use SCQA to reconstruct the author's narrative logic.
   - Use pyramid structure to group claims into main idea, subclaims, and details.

4. Test the argument
   - For each important claim, identify evidence, warrant, assumptions, limitations, and counterarguments.
   - Distinguish descriptive claims, causal claims, normative claims, and practical recommendations.

5. Teach for understanding
   - Explain difficult concepts in three layers: plain language, technical version, and example/analogy.
   - In `coach` mode, ask the user to explain the idea back, then diagnose one gap at a time.

6. Build memory
   - Generate active-recall questions before flashcards.
   - Create cards only for durable knowledge: key concepts, distinctions, mechanisms, evidence, and application rules.
   - Include a short spaced-review plan.

7. Transfer
   - Show how the article changes decisions, mental models, product thinking, engineering choices, research direction, or writing.
   - End with "what I should remember" and "what I should do next".

## Output Rules

- Prefer compact tables for claims, evidence, assumptions, and flashcards.
- Cite source locations when available: page, section, heading, paragraph, figure, or quote snippet.
- Do not fabricate page numbers, author intent, or missing data.
- Do not produce a generic summary before identifying the central thesis.
- Keep the learner active: include questions, prompts, and short tasks.
- When the user asks for only a summary, still include the central thesis and evidence quality.

## References

Load only what is needed:

- `references/methods.md`: method definitions and when to use 5W2H, SCQA, Feynman, memory, and critique.
- `references/output-templates.md`: reusable output templates for `scan`, `deep`, `coach`, and `memory`.
- `references/article-types.md`: adjustments for research papers, technical blogs, business essays, reports, and product articles.
