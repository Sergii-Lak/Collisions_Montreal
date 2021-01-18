
# --------------- Import -------------------------
from file_func import func

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# ----------- Options Pandas for Pycharm --------------
pd.set_option('max_columns', 15)
pd.set_option('display.max_rows', 200)
pd.set_option('expand_frame_repr', False)
pd.set_option('large_repr', 'truncate')

# ---------------- Open CSV and created DataFrame--------------------------

FILE_DATA = "collisions_routieres.csv"

df = pd.read_csv(FILE_DATA)

# **********************************************************

df['CD_ECLRM'] = df['CD_ECLRM'].map({
    1: 'Jour et clarté',
    2: 'Jour et demi-obscurité',
    3: 'Nuit et chemin éclairé',
    4:'Nuit et chemin non éclairé'
})

c = df[(df['GRAVITE'] == 'Mortel')][['CD_ECLRM']]
res = c.groupby('CD_ECLRM').size().to_dict()
titres = list(res.keys())
data = list(res.values())

plt.style.use('grayscale')
fig, ax = plt.subplots(figsize=(15, 10), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data), wedgeprops={'linewidth':0.8, 'edgecolor':'black', 'width': 0.5}, startangle=-40, textprops=dict(color="w"), pctdistance=0.7)

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(titres[i], xy=(x, y), xytext=(1.35 * np.sign(x), 1.4 * y),
                horizontalalignment=horizontalalignment, **kw)


plt.setp(autotexts, size=8, weight="bold")
ax.set_title("Éclairement: Degré de clarté")
plt.show()
