
# --------------- Import -------------------------
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.dates import MonthLocator


# ----------- Options Pandas for Pycharm --------------
pd.set_option('max_columns', 15)
pd.set_option('display.max_rows', 200)
pd.set_option('expand_frame_repr', False)
pd.set_option('large_repr', 'truncate')

# ---------------- Open CSV and created DataFrame--------------------------

FILE_DATA = "collisions_routieres.csv"

df = pd.read_csv(FILE_DATA)

# *********************************************************
quantity_accident_par_jour = df.groupby('DT_ACCDN').size().reset_index()

fig, ax = plt.subplots(figsize=(15, 10))

ax.bar(quantity_accident_par_jour['DT_ACCDN'], quantity_accident_par_jour[0], label='Number of accidents per month')
loc = MonthLocator() # this locator puts ticks at regular intervals
ax.xaxis.set_major_locator(loc)
plt.xticks(rotation=90)

plt.style.use('Solarize_Light2')
plt.legend()
plt.title("Number of accidents per month")
plt.xlabel("Month")
plt.ylabel("Total accidents")
plt.tight_layout()
plt.show()