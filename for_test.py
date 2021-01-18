# --------------- Import -------------------------
from file_func import func
from file_func import series_convert
from file_func import percent_values_return_dict

import pandas as pd
from matplotlib import  pyplot as plt
from datetime import datetime as dt
import numpy as np

# ----------- Options Pandas for Pycharm --------------
pd.set_option('max_columns', 44)
pd.set_option('display.max_rows', 200)
pd.set_option('expand_frame_repr', False)
pd.set_option('large_repr', 'truncate')

# ------------ Options matplotlib ---------------------
#plt.style.use('bmh')

# ---------------- Open CSV and created DataFrame--------------------------

FILE_DATA = "collisions_routieres.csv"

df = pd.read_csv(FILE_DATA)

# a = df.groupby('DT_ACCDN').size().reset_index()
# b = df.groupby('DT_ACCDN').count()[['JR_SEMN_ACCDN']].reset_index()
#
# print(a[0])
# print(b)



#print(df[df["DT_ACCDN"] == '2012/01/01'])
#print(df.apply(pd.Series.nunique))
#print(df.groupby('DT_ACCDN').count()[['JR_SEMN_ACCDN']])

# a = df['GRAVITE'].unique()
# b = df[df['GRAVITE'] == 'Mortel'].groupby('JR_SEMN_ACCDN').size()
# df['CD_ECLRM'] = df['CD_ECLRM'].map({1: 'Jour et clarté', 2: 'Jour et demi-obscurité', 3: 'Nuit et chemin éclairé', 4:'Nuit et chemin non éclairé'})
# c = df[df['GRAVITE'] == 'Mortel'][['JR_SEMN_ACCDN', 'CD_ECLRM']]
# d = df[df['GRAVITE'] == 'Mortel'][['JR_SEMN_ACCDN']].value_counts()
# print(c.groupby('CD_ECLRM').size())

dict_CD_GENRE_ACCDN = {
31:"Collision avec véhicule routier",
32:"Collision avec piéton",
33:"Collision avec cycliste",
34:"Collision avec train",
35:"Collision avec chevreuil (cerf de Virginie)",
36:"Collision avec orignal/ours/caribou",
37:"Collision avec autre animal",
38:"Collision avec obstacle temporaire",
39:"Collision avec objet projeté/détaché",
40:"Objet fixe: lampadaire",
41:"Objet fixe: support/feu de signalisation",
42:"Objet fixe: poteau (service public)",
43:"Objet fixe: arbre",
44:"Objet fixe: section de glissière de sécurité",
45:"Objet fixe: atténuateur d’impact",
46:"Objet fixe: extrémité de glissière de sécurité",
47:"Objet fixe: pilier (pont/tunnel)",
48:"Objet fixe: amoncellement de neige",
49:"Objet fixe: bâtiment/édifice/mur",
50:"Objet fixe: bordure/trottoir",
51:"Objet fixe: borne-fontaine",
52:"Objet fixe: clôture/barrière",
53:"Objet fixe: fossé",
54:"Objet fixe: paroi rocheuse",
55:"Objet fixe: ponceau",
59:"Objet fixe: autre objet fixe",
71:"Sans collision: capotage",
72:"Sans collision: renversement",
73:"Sans collision: submersion/cours d’eau",
74:"Sans collision: feu/explosion",
75:"Sans collision: quitte la chaussée",
99:"Sans collision: autre"}



df['CD_GENRE_ACCDN'] = df['CD_GENRE_ACCDN'].map(dict_CD_GENRE_ACCDN)
gravite_mortel = df[(df['GRAVITE'] == 'Mortel')][['CD_GENRE_ACCDN']]
gravite_domages = df[(df['GRAVITE'] == 'Dommages matériels seulement') | (df['GRAVITE'] == 'Dommages matériels inférieurs au seuil de rapportage')][['CD_GENRE_ACCDN']]
gravite_grave = df[(df['GRAVITE'] == 'Grave')][['CD_GENRE_ACCDN']]
gravite_leger = df[(df['GRAVITE'] == 'Léger')][['CD_GENRE_ACCDN']]

# print(gravite_mortel.groupby('CD_GENRE_ACCDN').size().sort_values(ascending=False))
# print(gravite_grave.groupby('CD_GENRE_ACCDN').size().sort_values(ascending=False))
# print(gravite_leger.groupby('CD_GENRE_ACCDN').size().sort_values(ascending=False))
# print(gravite_domages.groupby('CD_GENRE_ACCDN').size().sort_values(ascending=False))


def date_selection(date_, col, df):
    df2 = df
    df2['DT_ACCDN'] = pd.to_datetime(df2['DT_ACCDN'])
    date_data = df2.loc[(df2[col] >= str(date_)) & (df2[col] < str(date_ + 1))]
    return date_data

df3 = df

df3['DT_ACCDN'] = pd.to_datetime(df3['DT_ACCDN'])


print(date_selection(2013, 'DT_ACCDN', df))

