# TFM_turistificacioBCN
En aquest repositori trobareu els principals datasets i codi utilitzat en el desenvolupament del Treball Final de Màster de Ciència de Dades "Anàlisi dels factors relacionats amb el turisme en els processos de gentrificació".

El repositori s'estructura en tres directoris:
1. Code: en aquesta carpeta trobareu els scripts que automatitzen tasques, així com tres notebooks per preprocessar les dades
2. Data: en aquesta carpeta trobareu altres tres carpetes que contenen els datasets originals descarregats de les diferents fonts de dades
3. Data_cleaning: en aquesta carpeta trobareu els datasets nets i preparats per treballar

## Code
Aquest directori consta dels següents arxius:
1. API_opendataBCN.py: script per descarregar automàticament les dades de la web OpenDataBCN d'acord amb les estadístiques que ajustem als paràmetres
2. API_opendataBCN_zips.py: igual que l'anterior, però per datasets que es troben en format comprimit
4. cleaningVars.py: script mitjançant el qual es redueixen les dimensions d'un dataset a escollir
5. mergeHUT.py: script que fusiona els diferents arxius csv originals de dades d'habitatges d'ús turístic en un únic arxiu csv
6. searchingNulls.py: script que detecta els datasets d'un directori que contenen valors nuls
7. IndexTuristificacio.ipynb: notebook amb totes les operacions realitzades per obtenir l'Índex de turistificació
8. aggregateVars.ipynb: notebook amb totes les operacions realitazades per obtenir el dataset agregat amb totes les fonts de dades
9. cleaningNulls.ipynb: notebook amb les operacions realitzades per netejar els valors nuls
10. prepareDatasetTableau.ipynb: notebook amb les operacions realitzades per donar format al dataset per importar a Tableau

## Data
Aquest directori conté altres tres directoris amb els datasets originals descarregats de les webs
1. HabitatgeGeneralitat: conté dos arxius csv amb dades de contractes de lloguer i preus de lloguer per barris i anys
2. OpenDataBCN: conté tots els arxius csv descarregats de la web OpenDataBCN
3. UN_IDH: conté un únic arxiu csv amb les dades de l'Índex de Desenvolupament Humà per països i anys

En aquest cas, cal esmentar que hi ha datasets que no es troben publicats per questions d'emmagatzematge.

## Data_cleaning
Aquest conté altres dos directoris amb els datasets processats
1. def_dataset, que conté tres arxius excel:
   a. bcnGentTableau.xlsx, amb les dades preparades per importar a Tableau
   b. gent_vars_bcn.xlsx, amb tots els indicadors agregats per barri i any
   c. unitats-administratives-barris.xlsx, amb codi, nom i geometries dels diferents barris de Barcelona, per a les visualitzacions georreferenciades de Tableau
2. selectedVars, que conté tots els arxius csv amb les variables seleccionades a partir dels datasets originals
