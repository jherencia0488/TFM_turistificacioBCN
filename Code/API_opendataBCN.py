
import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

def process_datasets(dataset_urls):
    """Configure an API to download a set of datasets combining all of them in a combined
    csv file called as param dataset_urls, in a folder with the same name, for any url in a list
    params:
    dataset_urls: list of urls to download datasets from"""

    for dataset_url in dataset_urls:
        url = f"https://opendata-ajuntament.barcelona.cat/data/ca/dataset/{dataset_url}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")

            download_links = []
            for link in soup.find_all("a", class_="heading", title=lambda title: title and "csv" in title.lower()):
                download_links.append(link["href"])

            if download_links:
                dataset_name = os.path.basename(dataset_url).split(".")[0]  # Get dataset name from URL

                # Create directory for the dataset
                folder = f"../Data/OpenDataBCN/{dataset_name}"
                os.makedirs(folder, exist_ok=True)
                all_dataframes = []
                for link in download_links:
                    resource_id = link.split("/")[-1].split(".")[0]  # Extract resource ID
                    api_url = f"https://opendata-ajuntament.barcelona.cat/data/api/action/datastore_search?id={resource_id}&limit=50000"
                    try:
                        api_response = requests.get(api_url)
                        api_response.raise_for_status()
                        api_data = api_response.json()

                        if api_data["success"] and "result" in api_data and "records" in api_data["result"]:
                            df = pd.DataFrame(api_data["result"]["records"])
                            all_dataframes.append(df)
                            print(f"Downloaded and processed: {resource_id}")
                        else:
                            print(f"Error: Invalid API response for {resource_id}")

                    except requests.exceptions.RequestException as e:
                        print(f"Error fetching API data for {resource_id}: {e}")
                    except Exception as e:
                        print(f"An error occurred while processing API data for {resource_id}: {e}")

                if all_dataframes:
                    combined_df = pd.concat(all_dataframes, ignore_index=True)
                    combined_df.to_csv(os.path.join(folder, f"{dataset_name}.csv"), index=False)
                    print(f"Combined CSV for {dataset_name} created successfully.")
                else:
                  print(f"No dataframes were created for {dataset_name}.")
            else:
                print(f"No download links found for {dataset_url}")

        except requests.exceptions.RequestException as e:
            print(f"Error fetching the URL {dataset_url}: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

# List of urls (you can change with your own URLs):
dataset_urls = ['pad_mdb_niv-educa-esta_edat-q_sexe',
          'pad_cdo_b_sexe_barri-des',
          'pad_emi_mdbas_sexe_edat-q_continent-m',
          'pad_mdbas_lloc-naix-pais_lloc-naix-continent_sexe',
          'pad_sol_mdb_sexe_edat-q',
          'renda-tributaria-per-persona-atlas-distribucio',
          'atles-renda-index-gini',
          'est-cadastre-edificacions-edat-mitjana',
          'allotjaments-pensions',
          'allotjaments-hotels',
          'allotjaments-altres',
          'cens-locals-planta-baixa-act-economica',
          'cens-activitats-comercials',
          'terrasses-comercos-vigents',
          'equipament-restaurants',
          'equipaments-culturals-icub',
          'culturailleure-bibliotequesimuseus',
          'culturailleure-espaismusicacopes',
          'punts-informacio-turistica',
          'dades-festivals',
          'dades-arts-esceniques',
          'dades-museus-exposicions',
          'aforaments-detall',
          'culturailleure-espaisparticipaciociutadana',
          'pad-dimensions',
          'cens-activitats-economiques-class-bcn',
          'est-superficie',
          'xarxasoroll-equipsmonitor-instal',
          'aforaments-descriptiu',
          'pad_mdba_sexe_edat-1']

process_datasets(dataset_urls)