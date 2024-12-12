import pandas as pd
import os
from pandas.io.formats.format import return_docstring
import glob

os.path.isdir("../Data/OpenDataBCN/habitatges-us-turistic")
for name in os.listdir("../Data/OpenDataBCN/habitatges-us-turistic"):
    year = name[:4]
    try:
        df = pd.read_csv(f"../Data/OpenDataBCN/habitatges-us-turistic/{name}", sep=",", quotechar='"')
        df['Any'] = year
        df.to_csv(f"../Data/OpenDataBCN/habitatges-us-turistic/{name}", index=False)
    except FileNotFoundError:
        print(f"Error: file {name} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

try:
    all_huts_csv = glob.glob("../Data/OpenDataBCN/habitatges-us-turistic/*.csv")
    if not all_huts_csv:
        print(f"Error: no CSV files found.")

    df_list = []
    for file in all_huts_csv:
        try:
            df = pd.read_csv(file)
            df_list.append(df)
        except pd.errors.EmptyDataError:
            print(f"Warning: Skipping empty file: {file}")
        except pd.errors.ParserError:
            print(f"Warning: Skipping file with parser error: {file}")

    if not df_list:
        print("No valid CSV files to merge.")

    merged_df = pd.concat(df_list, ignore_index=True)
    merged_df.to_csv("../Data/OpenDataBCN/habitatges-us-turistic/habitatges-us-turistic.csv", index=False)
    print(f"CSV files merged and saved")
except Exception as e:
    print(f"An error occurred: {e}")

for file in all_huts_csv:
    try:
        os.remove(file)
        print(f"File {file} removed")
    except OSError as e:
        print(f"An error occurred: {e}")

