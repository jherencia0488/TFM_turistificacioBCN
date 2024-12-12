import pandas as pd
from pandas.io.formats.format import return_docstring

#Pregunta pel nom de l'arxiu a tractar
file = input("Introdueix el nom de l'arxiu a netejar, sense l'extensió .csv (exemple dades):")
path = f"../Data/OpenDataBCN/{file}/{file}.csv"

#El carrega com a dataframe
df = pd.read_csv(path, low_memory=False)

#Imprimeix una mostra de les dades
print(df.head(5))

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
df.to_csv(f"../Data_cleaning/selectedVars/{file}.csv", index=False)





