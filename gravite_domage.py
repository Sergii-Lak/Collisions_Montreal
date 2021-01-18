# --------------- Import -------------------------

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