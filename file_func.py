import numpy as np
import pandas as pd



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
99:"Sans collision: autre"
}

dict_CD_COND_METEO = {
    11:"Clair",
    12:"Couvert (nuageux/sombre)",
    13:"Brouillard/brume",
    14:"Pluie/bruine",
    15:"Averse (pluie forte)",
    16:"Vent fort",
    17 :"Neige/grêle",
    18 :"Poudrerie/tempête de neige",
    19 :"Verglas",
    99 :"Autre"
}

dict_CD_SIT_PRTCE_ACCDN = {
    1:"Déversement",
    2:"Perte de chargement",
    3:"Opération de déneigement",
    9:"Autre"
}

dict_CD_ETAT_SURFC = {
    11:"Sèche",
    12:"Mouillée",
    13:"Accumulation d’eau (aquaplanage)",
    14:"Sable, gravier sur la chaussée",
    15:"Gadoue/neige fondante",
    16:"Enneigée",
    17:"Neige durcie",
    18:"Glacée",
    19:"Boueuse",
    20:"Huileuse",
    99:"Autre"
}


def two_columns(data_frame, column_unique, column_result):
    d = dict()
    for i in data_frame[column_unique].unique():
        a = data_frame[data_frame[column_unique] == i]
        b = a[column_result].sum()
        d[i] = b
    d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
    return d

# def count_elements(data_frame, column_unique, column_result):
#     d = dict()
#     for i in data_frame[column_unique].unique():
#         a = data_frame[data_frame[column_unique] == i]
#         b = a[column_result].count()
#         d[i] = b
#     d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
#     return d

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d})".format(pct, absolute)

def count_in_column_to_dict(df, col):
    ccc = df[col].value_counts()
    return ccc.to_dict()

def count_in_column_to_list(df, col):
    ccc = df[col].value_counts()
    return ccc.tolist()

def series_convert(series, min_item):
    new_dict = dict()
    new_total_value = 0
    for t in series:
        if series[t] > min_item:
            new_dict[t] = series[t]
        elif series[t] <= min_item:
            new_total_value += series[t]
    new_dict['Autres'] = new_total_value
    return new_dict

def percent_values_return_dict(dict_1):
    total = sum(dict_1.values())
    new_dict = dict()
    for i in dict_1:
        new_dict[i] = round(((dict_1[i] / total)), 2)
    return new_dict

def date_selection(date_, col, df):
    df2 = df
    df2['DT_ACCDN'] = pd.to_datetime(df2['DT_ACCDN'])
    date_data = df2.loc[(df2[col] >= str(date_)) & (df2[col] < str(date_ + 1))]
    return date_data