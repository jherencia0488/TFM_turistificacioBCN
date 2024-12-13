import pandas as pd
import os

#Create a list with the name of the csv files in the selected folder that contains any nulls values, and print them on screen
datasets_nas = []
os.path.isdir("../Data_cleaning/selectedVars")
for name in os.listdir("../Data_cleaning/selectedVars"):
    df = pd.read_csv(f"../Data_cleaning/selectedVars/{name}")
    if df.isna().any().any():
        datasets_nas.append(name)

print("Datasets que contenen valors nuls:")
print(datasets_nas)
print(len(datasets_nas))
