# --------------- Import -------------------------
from file_func import two_columns

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

# *********************************************************
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