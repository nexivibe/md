#!/usr/bin/env python3
"""pdfize.py — Convert markdown medical reports to professionally formatted PDFs.

Usage:
    ./pdfize.py reports/Jeff.strategy.md
    ./pdfize.py reports/Jeff.strategy.md -o custom_output.pdf

Requires: pandoc, pdflatex (texlive)
"""

import sys
import os
import subprocess
import tempfile
import shutil
import argparse
from pathlib import Path
from datetime import date

LATEX_TEMPLATE = r"""\documentclass[11pt,letterpaper]{article}

% ── Geometry ──────────────────────────────────────────────────────────────────
\usepackage[margin=1in,top=1.25in,bottom=1.25in]{geometry}

% ── Fonts ─────────────────────────────────────────────────────────────────────
\usepackage[T1]{fontenc}
\usepackage{newpxtext}
\usepackage{newpxmath}
\usepackage{microtype}

% ── Colors ────────────────────────────────────────────────────────────────────
\usepackage{xcolor}
\definecolor{navy}{HTML}{1B3A5C}
\definecolor{accentblue}{HTML}{2C5F8A}
\definecolor{darktext}{HTML}{2D2D2D}
\definecolor{medgray}{HTML}{666666}
\definecolor{rulecolor}{HTML}{BBBBBB}
\definecolor{lightbg}{HTML}{F4F6F8}
\definecolor{quotebar}{HTML}{2C5F8A}

% ── Body text color ──────────────────────────────────────────────────────────
\color{darktext}

% ── Section formatting ───────────────────────────────────────────────────────
\usepackage{titlesec}
\setcounter{secnumdepth}{0}

\titleformat{\section}
  {\Large\bfseries\color{navy}}
  {}{0em}{}[\vspace{0.3ex}{\color{rulecolor}\titlerule}]
\titleformat{\subsection}
  {\large\bfseries\color{accentblue}}
  {}{0em}{}
\titleformat{\subsubsection}
  {\normalsize\bfseries\color{navy}}
  {}{0em}{}

\titlespacing*{\section}      {0pt}{2.5ex plus 1ex minus .2ex}{1.5ex plus .2ex}
\titlespacing*{\subsection}   {0pt}{2.0ex plus .8ex minus .2ex}{1.0ex plus .2ex}
\titlespacing*{\subsubsection}{0pt}{1.5ex plus .6ex minus .2ex}{0.8ex plus .2ex}

% ── Lists ─────────────────────────────────────────────────────────────────────
\usepackage{enumitem}
\setlist[itemize]{leftmargin=1.5em, itemsep=0.25em, parsep=0.1em, topsep=0.4em}
\setlist[enumerate]{leftmargin=1.5em, itemsep=0.25em, parsep=0.1em, topsep=0.4em}
\setlist[itemize,1]{label=\textcolor{accentblue}{\textbullet}}
\setlist[itemize,2]{label=\textcolor{medgray}{\textendash}}

% ── Header / Footer ──────────────────────────────────────────────────────────
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\color{medgray}\textsc{$header-title$}}
\fancyhead[R]{\small\color{medgray}\textsc{Personal Health Strategy}}
\fancyfoot[C]{\small\color{medgray}— \thepage\ —}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}
\renewcommand{\headrule}{\hbox to\headwidth{\color{rulecolor}\leaders\hrule height \headrulewidth\hfill}}

% ── First page style (no header) ─────────────────────────────────────────────
\fancypagestyle{plain}{
  \fancyhf{}
  \fancyfoot[C]{\small\color{medgray}— \thepage\ —}
  \renewcommand{\headrulewidth}{0pt}
}

% ── Tables ────────────────────────────────────────────────────────────────────
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage{calc}

% ── Hyperlinks ────────────────────────────────────────────────────────────────
\usepackage{hyperref}
\hypersetup{
  colorlinks=true,
  linkcolor=accentblue,
  urlcolor=accentblue,
  citecolor=accentblue,
  pdftitle={$title$},
}

% ── Graphics ──────────────────────────────────────────────────────────────────
\usepackage{graphicx}

% ── Block quotes (styled as callout sidebar) ──────────────────────────────────
\usepackage{mdframed}
\renewenvironment{quote}{%
  \begin{mdframed}[
    backgroundcolor=lightbg,
    linewidth=3pt,
    linecolor=quotebar,
    topline=false,
    bottomline=false,
    rightline=false,
    innerleftmargin=12pt,
    innerrightmargin=12pt,
    innertopmargin=10pt,
    innerbottommargin=10pt,
    skipabove=\topsep,
    skipbelow=\topsep
  ]\color{darktext}%
}{%
  \end{mdframed}%
}

% ── Pandoc compatibility ──────────────────────────────────────────────────────
\providecommand{\tightlist}{%
  \setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}

% ── Paragraph spacing ────────────────────────────────────────────────────────
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.5em plus 0.1em minus 0.1em}

% ══════════════════════════════════════════════════════════════════════════════
\begin{document}
\thispagestyle{plain}

% ── Title Block ───────────────────────────────────────────────────────────────
\begin{center}
  \vspace*{0.5em}
  {\color{navy}\rule{\textwidth}{2pt}}\\[1.8em]
  {\fontsize{26}{31}\selectfont\bfseries\color{navy} $title$}\\[0.9em]
  {\large\color{medgray} $subtitle$}\\[0.5em]
  {\normalsize\color{medgray} Prepared $date$}\\[1.4em]
  {\color{navy}\rule{\textwidth}{2pt}}
\end{center}
\vspace{1.5em}

% ── Body ──────────────────────────────────────────────────────────────────────
$body$

% ── Disclaimer Footer ────────────────────────────────────────────────────────
\vfill
\begin{center}
  {\color{rulecolor}\rule{0.6\textwidth}{0.4pt}}\\[0.8em]
  {\small\color{medgray}\textit{%
    This document is for informational purposes only and does not constitute medical advice.\\
    Always consult with qualified healthcare providers before making changes to your health regimen.}}
\end{center}

\end{document}
"""


def check_dependencies():
    """Verify that pandoc and pdflatex are installed."""
    missing = []
    for cmd in ("pandoc", "pdflatex"):
        if shutil.which(cmd) is None:
            missing.append(cmd)
    if missing:
        print(
            f"Error: missing required program(s): {', '.join(missing)}\n"
            f"Install with: sudo apt install pandoc texlive-latex-recommended texlive-latex-extra texlive-fonts-extra",
            file=sys.stderr,
        )
        sys.exit(1)


def extract_metadata(filepath):
    """Derive title fields from the filename (e.g. Jeff.strategy.md)."""
    stem = Path(filepath).stem  # "Jeff.strategy"
    parts = stem.split(".")
    patient = parts[0] if parts else "Patient"
    return {
        "title": f"{patient} — Personal Health Strategy",
        "subtitle": "Integrative Medical Case Review",
        "header-title": f"{patient} Health Strategy",
        "date": date.today().strftime("%B %d, %Y"),
    }


def build_pdf(input_path, output_path, metadata):
    """Run pandoc to convert markdown → PDF via the embedded LaTeX template."""
    tmpdir = tempfile.mkdtemp(prefix="pdfize_")
    try:
        # Write the template into the temp directory
        tpl = os.path.join(tmpdir, "medical.latex")
        with open(tpl, "w") as f:
            f.write(LATEX_TEMPLATE)

        cmd = [
            "pandoc",
            str(input_path),
            "-o",
            str(output_path),
            "--from",
            "markdown-tex_math_dollars",
            "--template",
            tpl,
            "--pdf-engine",
            "pdflatex",
            "--highlight-style",
            "kate",
        ]
        for key, val in metadata.items():
            cmd += ["-V", f"{key}={val}"]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            print(f"Error: pandoc failed\n{result.stderr}", file=sys.stderr)
            sys.exit(1)

        print(f"  ✓ {output_path}")

    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


def main():
    parser = argparse.ArgumentParser(
        description="Convert markdown medical reports to professionally formatted PDFs via LaTeX.",
    )
    parser.add_argument("input", nargs="+", help="One or more markdown files to convert")
    parser.add_argument(
        "-o",
        "--output",
        help="Output PDF path (only valid with a single input file)",
    )
    args = parser.parse_args()

    if args.output and len(args.input) > 1:
        print("Error: -o/--output can only be used with a single input file", file=sys.stderr)
        sys.exit(1)

    check_dependencies()

    for md_file in args.input:
        input_path = Path(md_file).resolve()
        if not input_path.exists():
            print(f"Error: file not found: {input_path}", file=sys.stderr)
            sys.exit(1)
        if not input_path.suffix.lower() == ".md":
            print(f"Warning: {input_path.name} does not look like a markdown file", file=sys.stderr)

        if args.output:
            output_path = Path(args.output).resolve()
        else:
            output_path = input_path.with_suffix(".pdf")

        metadata = extract_metadata(input_path)
        build_pdf(input_path, output_path, metadata)


if __name__ == "__main__":
    main()
