import requests
from bs4 import BeautifulSoup
import os
import zipfile
import glob
import pandas as pd
from urllib.parse import urlparse


def download_zip_files(url):
    """
    Downloads all zip files from a given URL that have a download link.
    Saves combined CSV in a folder named after the last part of the URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        download_links = []

        for link in soup.find_all('a', href=True):
            if link['href'].endswith('download'):
                download_links.append(link['href'])

        parsed_url = urlparse(url)
        last_part_url = os.path.basename(parsed_url.path) or os.path.basename(parsed_url.netloc)
        output_dir = f"../Data/OpenDataBCN/{last_part_url}"

        os.makedirs(output_dir, exist_ok=True)  # Create the directory

        for link in download_links:
            if link.startswith("http"):
                file_url = link
            else:
                file_url = url + link if url.endswith("/") else url + "/" + link

            try:
                file_response = requests.get(file_url, stream=True)
                file_response.raise_for_status()

                filename = os.path.basename(file_url)
                filepath = os.path.join(output_dir, filename)

                with open(filepath, 'wb') as file:
                    for chunk in file_response.iter_content(chunk_size=8192):
                        file.write(chunk)

                print(f"Downloaded: {filename} to {output_dir}")

                try:
                    with zipfile.ZipFile(filepath, 'r') as zip_ref:
                        zip_ref.extractall(output_dir)
                    print(f"Extracted: {filename} to {output_dir}")
                except zipfile.BadZipFile:
                    print(f"Warning: {filename} is not a valid zip file or corrupted.")

            except requests.exceptions.RequestException as e:
                print(f"Error downloading {link}: {e}")

    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")

    merge_csv_files(output_dir)  # Merge in the specific output directory


def merge_csv_files(directory):
    csv_files = glob.glob(os.path.join(directory, "*.csv"))
    if not csv_files:
        print(f"No CSV files found in {directory}")
        return

    merged_df = pd.DataFrame()
    for file in csv_files:
        try:
            df = pd.read_csv(file, encoding='utf-8', sep=',')
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        except pd.errors.ParserError:
            print(f"Warning: Could not parse {file}. Skipping.")
        except Exception as e:
            print(f"Error reading {file}: {e}")

    if not merged_df.empty:
        merged_filename = os.path.basename(directory) + ".csv"  # Use directory name as filename
        merged_filepath = os.path.join(directory, merged_filename)
        merged_df.to_csv(merged_filepath, index=False, encoding='utf-8')
        print(f"Merged CSV files into: {merged_filepath}")
    else:
        print("No valid CSV data to merge.")

def delete_files_except_merged(directory):
    """Deletes all files in a directory except the merged CSV file."""
    merged_file = os.path.join(directory, os.path.basename(directory) + ".csv")
    for filename in glob.glob(os.path.join(directory, "*")):
        if filename != merged_file:
            try:
                if os.path.isfile(filename):
                    os.remove(filename)
                    print(f"Deleted file: {filename}")
                elif os.path.isdir(filename):
                    print(f"Directory found: {filename} - Not deleted.")
            except OSError as e:
                print(f"Error deleting {filename}: {e}")

# You can change the URL if needed
url = "https://opendata-ajuntament.barcelona.cat/data/es/dataset/xarxasoroll-equipsmonitor-dades"
download_zip_files(url)

# Delete non combined csv files
delete_files_except_mergec("xarxasoroll-equipsmonitor-dades")