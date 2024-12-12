import pandas as pd
from pandas.io.formats.format import return_docstring

#El carrega com a dataframe
df = pd.read_csv("../Data/HabitatgeGeneralitat/anual_bcn_lloguer_m2.csv", sep=";", encoding="utf-8")

#Imprimeix una mostra de les dades
print(df.head(5))
columns = ['2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014']
for i in columns:
    df[i] = df[i].astype(str).str.replace(',', '.')
#Imprimeix les columnes i el seu índex
print("Columnes del dataset:")
for i, col in enumerate(df.columns):
    print(f"{i}: {col}")

variables = input("Introdueix els índex de les columnes que vols mantenir separades per comes:")
variables = [int(x.strip()) for x in variables.split(",") if x.strip()]

if not all(0 <= i < len(df.columns) for i in variables):
    print("Index de columnes no vàlids.")

selected_cols = [df.columns[i] for i in variables]
df = df[selected_cols]
df.to_csv(f"../Data_cleaning/selectedVars/anual_bcn_lloguer_m2.csv", index=False)