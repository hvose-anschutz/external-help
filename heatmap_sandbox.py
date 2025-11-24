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
ax.imshow(values, extent=[0,12,0,4], interpolation="none", cmap='viridis')

# Example labels
ylabels = ["Adipose","Cecum","Liver","Spleen"]
xlabels = ["a","b","c","d","e","f","g","h","i","j","k","l"]
nylabels= ["r1","r2","r1","r2","r1","r2","r1","r2"]
nxlabels= [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3]

# Create a "new" y-axis that shares the same spacing and data as the current x-axis,
# making it plottable on the right side of the graph.
new_ax = ax.twinx().twiny()
#new_x = ax.twiny()

# Configure tick labels to be in the range of 0 to # cols and rows accordingly
ax.set_xticks(np.arange(0, M),labels=xlabels)
ax.set_xticks(np.arange(-0.5, M + 0.5, 1), minor=True)
ax.set_yticks(np.arange(0, N),labels=ylabels)
ax.set_yticks(np.arange(-0.5, N + 0.5, 1), minor=True)

# Configure new y axis
new_ax.set_xticks(np.arange(0, 2*M,1),labels=nxlabels)
new_ax.set_xticks(np.arange(-0.5, 2*M + 0.5,1), minor=True)
new_ax.set_yticks(np.arange(0, 2*N,1),labels=nylabels)
new_ax.set_yticks(np.arange(-0.5, 2*N + 0.5, 1), minor=True)

# Other configurations (box-defining borders, tick length, etc...)
new_ax.grid(which='minor', lw=2, color='white', clip_on=False)
ax.grid(which='minor', lw=2, color='white', clip_on=False)
ax.tick_params(length=0)
new_ax.tick_params(length=0)
new_ax.invert_yaxis()
#ax.set_aspect('equal',adjustable='datalim')

# Turning off original graph spines so they don't overlap

# Show the plot (it doesn't look right)
plt.savefig('broken_plot.png',dpi=300,bbox_inches='tight')
#plt.show()
