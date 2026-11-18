# Scientific animations with Manim

A side project that unites my love for natural sciences and programming.

Python scenes visualizing biochemical processes using [Manim Community](https://www.manim.community/) and LaTeX chemical diagrams.

## Contents

- `glycolysis.py` — glycolysis animation (`Glycolysis` scene).
- `fermentation.py`, `fermentation_full.py`, `fermentation_acetate.py`, `fermentation_ethanol.py`, `fermentation_lactate.py` — fermentation-related visualizations.
- `media/` — generated output assets, where committed.

The animations use Estonian scientific terminology and chemical structures typeset with `chemfig`.

## Getting started

Install [Manim Community](https://docs.manim.community/en/stable/installation.html), a working LaTeX distribution, and the LaTeX `chemfig` package. Manim's rendering dependencies (including FFmpeg) must also be available.

```bash
manim -pql glycolysis.py Glycolysis
```
