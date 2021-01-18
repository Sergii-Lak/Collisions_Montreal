# --------------- Import -------------------------
from file_func import two_columns
#from file_func import count_elements
from file_func import dict_CD_GENRE_ACCDN

import pandas as pd
from matplotlib import  pyplot as plt
from datetime import datetime as dt
import numpy as np

# ----------- Options Pandas for Pycharm --------------
pd.set_option('max_columns', 15)
pd.set_option('display.max_rows', 200)
pd.set_option('expand_frame_repr', False)
pd.set_option('large_repr', 'truncate')

# ---------------- Open CSV and created DataFrame--------------------------

FILE_DATA = "collisions_routieres.csv"

df = pd.read_csv(FILE_DATA)

# -------------------- coding -----------------------------
# *********************************************************
#                    Time of the accident.
#   Interval of 60 minutes, containing the actual time of the accident.
#                 Example: 20:00:00-20:59:59

result1 = two_columns(df, "HEURE_ACCDN", "NB_VICTIMES_TOTAL")
result1_sorted_by_heures = dict(sorted(result1.items()))

hour_accident_x = list(result1_sorted_by_heures.keys())
nombre_victims_y = list(result1_sorted_by_heures.values())
list_str_hours = []
for hour_item in hour_accident_x:
    if hour_item == "Non précisé":
        list_str_hours.append(hour_item)
    else:
        el = str(hour_item).replace(":00-", "-")
        el = str(el).replace("59:00", "59")
        list_str_hours.append(el)

plt.style.use('bmh')
plt.bar(list_str_hours, nombre_victims_y, color="#444444", label="Victims")
plt.xticks(rotation=90)
plt.legend()
plt.title("Victims in road accidents in Montreal(2012 - 2019)")
plt.xlabel("Time of day")
plt.ylabel("Total victims")
plt.tight_layout()
plt.show()

print(plt.style.available)

# **********************************************************
# Total victims par jour de la semaine

result2 = two_columns(df, "JR_SEMN_ACCDN", "NB_VICTIMES_TOTAL")
result2['SA'] = result2.pop('SA')


day_accident_x = list(result2.keys())
nombre2_victims_y = list(result2.values())

plt.style.use('seaborn-bright')
plt.bar(day_accident_x, nombre2_victims_y, color="#333333", label="Victims")
plt.xticks(rotation=90)
plt.legend()
plt.title("Victims in road accidents in Montreal(2012 - 2019)")
plt.xlabel("Day")
plt.ylabel("Total victims")
plt.tight_layout()
plt.show()

# **********************************************************

result3 = []
for item in df['GRAVITE'].unique():
    a = df[df['GRAVITE'] == item]
    b = a['GRAVITE'].count()
    result3.append(b)


labels = list(df['GRAVITE'].unique())
labels[0] = 'Dommages <= 2000$'
labels[1], labels[4] = labels[4], labels[1]
slices = result3
slices[1], slices[4] = slices[4], slices[1]
explode = [0.1, 0.1, 0.1, 0.1, 0.1]

plt.style.use('bmh')
font = {
        'weight' : 'bold',
        'size'   : 15}
plt.rc('font', **font)
plt.figure(figsize=(15, 10))
plt.pie(slices, labels=labels, explode=explode, shadow=True, startangle=90, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'}, labeldistance=1.1)

plt.title("Gravité de l’accident:", )
plt.tight_layout()
plt.show()


# **********************************************************

# quantity_accident_par_jour = df.groupby('DT_ACCDN').size().reset_index()
#
# plt.style.use('Solarize_Light2')
# plt.bar(quantity_accident_par_jour['DT_ACCDN'], quantity_accident_par_jour[0], color="#222222", label='Number of accidents per day')
# plt.xticks(visible = False)
# plt.legend()
# plt.title("Number of accidents per day")
# plt.xlabel("Day")
# plt.ylabel("Total accidents")
# plt.tight_layout()
# plt.show()


# **********************************************************

# df2 = df
# df2['CD_GENRE_ACCDN'] = df2['CD_GENRE_ACCDN'].map(dict_CD_GENRE_ACCDN)
# gravite_mortel = df2[(df2['GRAVITE'] == 'Mortel')][['CD_GENRE_ACCDN']]
# gravite_domages = df2[(df2['GRAVITE'] == 'Dommages matériels seulement') | (df2['GRAVITE'] == 'Dommages matériels inférieurs au seuil de rapportage')][['CD_GENRE_ACCDN']]
# gravite_grave = df2[(df2['GRAVITE'] == 'Grave')][['CD_GENRE_ACCDN']]
# gravite_leger = df2[(df2['GRAVITE'] == 'Léger')][['CD_GENRE_ACCDN']]
#
# plt.figure(figsize=(10, 12))
# gm = gravite_leger.groupby('CD_GENRE_ACCDN').size().sort_values(ascending=False)
# gm.plot.barh()
# plt.show()

# **********************************************************

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d})".format(pct, absolute)

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
fig, ax = plt.subplots(figsize=(5, 3), subplot_kw=dict(aspect="equal"))

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
