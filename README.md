This repo is like a sandbox but more structured for specific issues.

# CURRENT ISSUES

### heatmap_sandbox.py

**ISSUE**: I need to graph a heatmap that has labels on all four axes (left, bottom, right, top) with slightly different spacing.
The idea is that the left and bottom axes represent larger categories (i.e. Tissues and Infection types) while the right and top
axes represent sample subsets (i.e. Replicate and Mouse Number). Currently, my plan is to graph each value individually, and then
use `matplotlib` functions to manually space the ticks out. Unfortunately, this seems to either be a bug or I'm just using the
wrong functionality.

**PICTURE OF ERROR**

![Most recent plot](https://github.com/hvose-anschutz/external-help/broken_plot.png,"broken plot")