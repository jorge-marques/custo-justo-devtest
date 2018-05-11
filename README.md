# Introduction

This is a simple exercise that should take around 30m, depending on your ease with the language you choose -- don't worry too much if it takes you a bit longer, though.

It should be done in either:
- C
- python
- php
- go

Please use only standard libraries (`stdlib.h`, `regex.h`, no PIP/PEAR, etc.).

If anything non-stardard is needed to compile/run, please let us know/provide instructions.

The code should be [clear and objective](1); and don't worry _too much_ about [optimizations](2).

Please send all source files (no binaries) needed to run the exercise in a single `zip` or `tar`.

# Description

Using your chosen language, read/parse `categories.txt` and write:

1. a function to check (by the ID) whether a category is a leaf category (no children).

> Example: `is_leaf(6140)` (Livros) should return `true`, while `is_leaf(6000)` (Desporto & Lazer) should return `false`.

2. a function to list leaf categories (sort ascending, by ID).

3. a function to return categories whose name (or part of it) match a given string.

Examples:
- `match("des")` should return `["Descapotável / Coupé (2022)", "Têxteis lar & Utilidades (5140)", "Desporto & Lazer (6000)", "Antiguidades e Colecções (6010)", "Artigos desporto (6040)"]`, and:
- `match("ar")` should return `["Imobiliário (1000)", "Para a Casa & Vestuário (5000)", "Vestuário (5020)", "Vestuário bebé & criança (5080)"]`

[1]: http://va.lent.in/optimize-for-readability-first/
[2]: http://wiki.c2.com/?PrematureOptimization
