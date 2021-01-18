
# --------------- Import -------------------------
from file_func import date_selection


import pandas as pd
from matplotlib import  pyplot as plt

# ----------- Options Pandas for Pycharm --------------
pd.set_option('max_columns', 44)
pd.set_option('display.max_rows', 200)
pd.set_option('expand_frame_repr', False)
pd.set_option('large_repr', 'truncate')

# ---------------- Open CSV and created DataFrame--------------------------

FILE_DATA = "collisions_routieres.csv"

df = pd.read_csv(FILE_DATA)

# *************************************************

list_global = []
dict_semain = dict()
for i in range(2012, 2020):
    res = date_selection(i, 'DT_ACCDN', df)
    sub_res = res["JR_SEMN_ACCDN"].value_counts().to_dict()
    list_global.append([sub_res['DI'], sub_res['LU'], sub_res['MA'], sub_res['ME'], sub_res['JE'], sub_res['VE'], sub_res['SA']])
print(list_global)


_2012 = list_global[0]
_2013 = list_global[1]
_2014 = list_global[2]
_2015 = list_global[3]
_2016 = list_global[4]
_2017 = list_global[5]
_2018 = list_global[6]
_2019 = list_global[7]

activity = ['DI', 'LU', 'MA', 'ME', 'JE', 'VE', 'SA']


plt.style.use('bmh')
fig, ax = plt.subplots()
ax.plot(activity, _2012, label="2012", marker='o')
ax.plot(activity, _2013, label="2013", marker='o')
ax.plot(activity, _2014, label="2014", marker='o')
ax.plot(activity, _2015, label="2015", marker='o')
ax.plot(activity, _2016, label="2016", marker='o')
ax.plot(activity, _2017, label="2017", marker='o')
ax.plot(activity, _2018, label="2018", marker='o')
ax.plot(activity, _2019, label="2019", marker='o')

plt.grid(True)
plt.legend()
plt.title("Number of accidents per day of week")
plt.xlabel("day of week")
plt.ylabel("Total number accidents")
plt.tight_layout()
ax.legend()

plt.show()