#!/usr/bin/env python3

"""Creates a heatmap with labels on all four axes. Or at least it should,
but it's broken right now."""

from matplotlib import pyplot as plt
import numpy as np

# DEFINING SIZE OF PLOTS
# Size of overarching categories (12 columns, 4 rows)
M, N = 12, 4

# Size of individual subplots (1 row, 5 columns PER LARGER CELL)
L, K = 1, 5

# Generate random heatmap values between 0 and 100 at the correct size
values = np.random.uniform(0, 100, (N * L, M * K))

# Generate subplots for the figure
fig, ax = plt.subplots()
cax = ax.imshow(values, cmap='viridis')

# Example labels
ylabels = ["Adipose","Cecum","Liver","Spleen"]
xlabels = ["a","b","c","d","e","f","g","h","i","j","k","l"]

# Create a "new" y-axis that shares the same spacing and data as the current x-axis,
# making it plottable on the right side of the graph.
new_y = ax.twinx()
#new_x = ax.twiny()

# Configure tick labels to be in the range of 0 to # cols and rows accordingly
ax.set_xticks(np.arange(0, M),labels=xlabels)
ax.set_xticks(np.arange(-0.5, M), minor=True)
ax.set_yticks(np.arange(0, N),labels=ylabels)
ax.set_yticks(np.arange(-0.5, N), minor=True)

# Configure new y axis
new_y.set_yticks(np.arange(0, N),labels=ylabels)
new_y.set_yticks(np.arange(-0.5, N), minor=True)

# Other configurations (box-defining borders, tick length, etc...)
#ax.grid(which='minor', lw=4, color='white', clip_on=False)
#ax.grid(which='major', lw=2, color='white', clip_on=False)
ax.tick_params(length=0)
#ax.set_aspect('equal',adjustable='datalim')

# Turning off original graph spines so they don't overlap
for s in ax.spines:
    ax.spines[s].set_visible(False)

# Show the plot (it doesn't look right)
plt.savefig('broken_plot.svg',dpi=300,bbox_inches='tight')
plt.show()
