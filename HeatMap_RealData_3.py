import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import sys
import re

sns.set_theme()

STAT_FILTER = True

myCSV = sys.argv[1]

df = pd.read_csv(myCSV,index_col = 0, header = 0) # reads in CSV as dataset

# Q1 = df.quantile(0.25)
# Q3 = df.quantile(0.75)

# IQR = Q3-Q1

# print(df.head())

# upper_bound = Q3 + (1.5 * IQR)

# df[df > upper_bound] = None

# print(upper_bound)

fig, ax = plt.subplots(figsize=(7, 7))

#lut = dict(zip(TnType.unique(), "rbg"))
#row_col = TnType.map(lut)
Pal = sns.light_palette("#bb334c", as_cmap=True) #Sets color palette to be in the range from White to a Saturated Color, should be set to the color of the year
# Draw the full plot
g = sns.heatmap(df
			, cmap = Pal
			, vmin = 0  #Sets the minimum value for the lowest saturation of the color bar
			, vmax = df.max().max()  #Sets the maximum value for the highest saturation of the color bar
            ,linewidths=.5
            #,figsize=(12, 30)
)

#plt.show()
#g.ax_row_dendrogram.remove()
fig = g.figure

myOutput = re.sub(".csv",".svg",myCSV)
fig.savefig(myOutput,dpi=300,bbox_inches="tight")