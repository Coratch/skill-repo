#!/usr/bin/env python3
"""Extract page-marked text from a PDF.

Tries pypdf first, then the `pdftotext` CLI if available.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def extract_with_pypdf(pdf_path: Path) -> str | None:
    try:
        from pypdf import PdfReader  # type: ignore
    except ImportError:
        return None

    reader = PdfReader(str(pdf_path))
    chunks: list[str] = []
    for index, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        chunks.append(f"\n\n--- Page {index} ---\n{text.strip()}")
    return "\n".join(chunks).strip()


def extract_with_pdftotext(pdf_path: Path) -> str | None:
    if shutil.which("pdftotext") is None:
        return None

    result = subprocess.run(
        ["pdftotext", "-layout", str(pdf_path), "-"],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "pdftotext failed")
    return result.stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract text from a PDF.")
    parser.add_argument("pdf", type=Path, help="Input PDF path")
    parser.add_argument("--output", "-o", type=Path, help="Output text path")
    args = parser.parse_args()

    pdf_path = args.pdf.expanduser().resolve()
    if not pdf_path.exists():
        print(f"PDF not found: {pdf_path}", file=sys.stderr)
        return 2

    try:
        text = extract_with_pypdf(pdf_path)
        if text is None:
            text = extract_with_pdftotext(pdf_path)
    except Exception as exc:
        print(f"PDF extraction failed: {exc}", file=sys.stderr)
        return 1

    if not text:
        print(
            "No extractor available or no text found. Install pypdf or pdftotext.",
            file=sys.stderr,
        )
        return 1

    if args.output:
        output_path = args.output.expanduser().resolve()
        output_path.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
