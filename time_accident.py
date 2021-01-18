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
plt.figure(figsize=(15, 10))
plt.bar(list_str_hours, nombre_victims_y, color="#444444", label="Victims")
plt.xticks(rotation=90)
plt.legend()
plt.title("Victims in road accidents in Montreal(2012 - 2019)")
plt.xlabel("Time of day")
plt.ylabel("Total victims")
plt.tight_layout()
plt.show()

print(plt.style.available)