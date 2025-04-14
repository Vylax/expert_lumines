- [ ] UPDATE the mail fetching using outlook API via azure

DENTEGO_rapport_generation:
TYPE_DE_DEPOT;TYPE_DE_FICHIER;FINESS;NUMLOT;DATE_DE_TT

df_dentego: faire un dataframe avec tt les rapports dentego
- **filtrer et retirer les rows dont l'attribut de la colonne TYPE_DE_DEPOT n'est pas "Tessi"**
- cast DATE_DE_TT en date avec dayFirst=True
- cast NUMLOT en int
- pas de cast sur finess?
- ajouter une colonne date_generation = date de creation du fichier rapport dentego dans les metadonnée (ou date du mail si possible)
df_tessi: faire un dataframe avec les rapports tessi en supprimant les lignes dupliquées
- cast filler_03 en date avec dayFirst=True
- cast nimmat en int
- pas de cast sur filler_05?

merged_df: joindre les 2 df sur les criteres suivants: (left join avec dentego a gauche)
- df_dentego.DATE_DE_TT = df_tessi.filler_03
- df_dentego.NUMLOT = df_tessi.nimmat
- df_dentego.FINESS = df_tessi.filler_05

creer un nouveau dataframe nommé df_delta:
- 4 colonnes:
	- DATE DE DEPOT
	- DENTEGO DEPOSE
	- TESSI TRAITE
	- DELTA
- df_delta a une ligne par valeur unique de date_generation dans df_dentego
- pour chaque ligne de df_delta, les valeurs sont: 
	- DATE DE DEPOT: df_dentego.date_generation
	- DENTEGO DEPOSE: le nb de lignes de df_dentego telles que date_generation=DATE DE DEPOT
	- TESSI TRAITE: le nb de lignes de merged_df telles que date_generation=DATE DE DEPOT
	- DELTA: DENTEGO DEPOSE - TESSI TRAITE

rapport excel:
- on le nomme "rapport_delta_YY-MM-DD_HH-MM-SS.xlsx"
- on le créer avec 2 pages: delta, merged
	- delta a les colonnes de df_delta et toutes les lignes de df_delta
	- merged a les colonnes de merged_df et toutes les lignes de merged_df

script:
(use function read_excel_file(filepath) to read excels and get a pd df)
- read all the excel files in the subfolders of folder dentego to create dentego_df by merging them and removing duplicate rows
- read all the excel files in the subfolders of folder tessi to create tessi_df by merging them and removing duplicate rows
- create merged_df
- create df_delta
- save rapport excel


======================

correctif:
pour df_delta:
TESSI_TRAITE est le nombre de lignes dans le merged_df dont la colonne "Date depot poste" vaut DATE DE DEPOT






=========================

df_dentego: faire un dataframe avec tt les rapports dentego
- **filtrer et retirer les rows dont l'attribut de la colonne TYPE_DE_DEPOT n'est pas "Tessi"**
- cast DATE_DE_TT en date avec dayFirst=True
- cast NUMLOT en int
- pas de cast sur finess?
- ajouter une colonne date_generation = date de creation du fichier rapport dentego dans les metadonnée (ou date du mail si possible)
df_tessi: faire un dataframe avec les rapports tessi en supprimant les lignes dupliquées
- cast filler_03 en date avec dayFirst=True
- cast nimmat en int
- pas de cast sur filler_05?

merged_df: joindre les 2 df sur les criteres suivants: (left join avec dentego a gauche)
- df_dentego.DATE_DE_TT = df_tessi.filler_03
- df_dentego.NUMLOT = df_tessi.nimmat
- df_dentego.FINESS = df_tessi.filler_05

creer un nouveau dataframe nommé df_delta:
- 5 colonnes:
	- DATE DE DEPOT
	- DENTEGO DEPOSE
	- TESSI TRAITE
	- DENTEGO_TESSI_EN_COMMUN
	- DELTA
	- DELTA_1
	- DELTA_2
- df_delta a une ligne par valeur unique de date dans l'ensembles des données (valeur de date dans df_dentego.date_generation ou df_tessi.filler_03)
- pour chaque ligne de df_delta, les valeurs sont: 
	- DATE DE DEPOT: la valeur unique de date
	- DENTEGO DEPOSE: le nb de lignes de df_dentego telles que date_generation=DATE DE DEPOT
	- TESSI TRAITE: le nb de lignes de df_tessi telles que filler_03=DATE DE DEPOT
	- DENTEGO_TESSI_EN_COMMUN: le nb de ligne de merged_df telles que date_generation=DATE DE DEPOT
	- DELTA: DENTEGO DEPOSE - TESSI TRAITE
	- DELTA_1: DENTEGO DEPOSE - DENTEGO_TESSI_EN_COMMUN
	- DELTA_2: TESSI TRAITE - DENTEGO_TESSI_EN_COMMUN

rapport excel:
- on le nomme "rapport_delta_YY-MM-DD_HH-MM-SS.xlsx"
- on le créer avec 2 pages: delta, merged
	- delta a les colonnes de df_delta et toutes les lignes de df_delta
	- merged a les colonnes de merged_df et toutes les lignes de merged_df

script:
(use function read_excel_file(filepath) to read excels and get a pd df)
- read all the excel files in the subfolders of folder dentego to create dentego_df by merging them and removing duplicate rows
- read all the excel files in the subfolders of folder tessi to create tessi_df by merging them and removing duplicate rows
- create merged_df
- create df_delta
- save rapport excel
