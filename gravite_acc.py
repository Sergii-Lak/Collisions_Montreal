from file_func import series_convert
from file_func import percent_values_return_dict
from matplotlib.patches import ConnectionPatch
import numpy as np

# --------------- Import -------------------------

from file_func import func

import pandas as pd
from matplotlib import pyplot as plt

# ----------- Options Pandas for Pycharm --------------
pd.set_option('max_columns', 15)
pd.set_option('display.max_rows', 200)
pd.set_option('expand_frame_repr', False)
pd.set_option('large_repr', 'truncate')

# ---------------- Open CSV and created DataFrame--------------------------

FILE_DATA = "collisions_routieres.csv"

df = pd.read_csv(FILE_DATA)
# -------------------- coding -----------------------------
gr = df['GRAVITE'].value_counts().to_dict()
titres = list(gr.keys())
titres[2], titres[3] = titres[3], titres[2]
data = list(gr.values())
data[2], data[3] = data[3], data[2]

gr = df[(df['GRAVITE']=='Mortel') | (df['GRAVITE'] =='Grave') | (df['GRAVITE'] == 'Léger')]
res01 = gr['CD_GENRE_ACCDN'].value_counts().to_dict()
subplot_data_dict = percent_values_return_dict(series_convert(res01, 1500))


# make figure and assign axis objects
fig = plt.figure(figsize=(9, 5))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
fig.subplots_adjust(wspace=0)

# pie chart parameters
ratios = data
labels = titres
explode = [0.1, 0.1, 0, 0, 0]
# rotate so that first wedge is split by the x-axis
angle = -180 * ratios[0]
ax1.pie(ratios, autopct=lambda pct: func(pct, data), startangle=angle, wedgeprops={'linewidth':0.8, 'edgecolor':'black'}, labels=labels, explode=explode)

# bar chart parameters

xpos = 0
bottom = 0
#ratios = [.56, .21, .13, .9]
ratios = list(subplot_data_dict.values())
width = .2
colors = [[.1, .3, .5], [.1, .3, .3], [.1, .3, .7], [.1, .3, .9]]

for j in range(len(ratios)):
    height = ratios[j]
    ax2.bar(xpos, height, width, bottom=bottom, color=colors[j])
    ypos = bottom + ax2.patches[j].get_height() / 2
    bottom += height
    #ax2.text(xpos, ypos, "%d%%" % (ax2.patches[j].get_height() * 100), ha='center')
    ax2.text(xpos, ypos, f"{round(ratios[j] * 100)}%", ha='center')

ax2.set_title('Genre d’accident')
#ax2.legend(('50-65', 'Over 65', '35-49', 'Under 35'))
ax2.legend(('véhicule', 'piéton', 'cycliste', 'Autres'))
ax2.axis('off')
ax2.set_xlim(- 2.5 * width, 2.5 * width)

# use ConnectionPatch to draw lines between the two plots
# get the wedge data
theta1, theta2 = ax1.patches[2].theta1, ax1.patches[4].theta2
center, r = ax1.patches[2].center, ax1.patches[1].r
bar_height = sum([item.get_height() for item in ax2.patches])

# draw top connecting line
x = r * np.cos(np.pi / 180 * theta2) + center[0]
y = r * np.sin(np.pi / 180 * theta2) + center[1]
con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
con.set_color([0, 0, 0])
con.set_linewidth(2)
ax2.add_artist(con)

# draw bottom connecting line
x = r * np.cos(np.pi / 180 * theta1) + center[0]
y = r * np.sin(np.pi / 180 * theta1) + center[1]
con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
con.set_color([0, 0, 0])
ax2.add_artist(con)
con.set_linewidth(2)

plt.show()