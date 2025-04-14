- [ ] paralléliser les calls PHP
- [ ] récupérer les bonnes données
- [ ] faire des appels en parallèles pour les filles et nous
- [ ] comparer les rapports tout les matins et relever les problemes
	- [x] faire un script
	- [ ] ajouter le dl automatique au script
	- [ ] ajouter la separation de la generation manuelle et automatique
	- [ ] ajouter le type d'erreur associé

I want a python script that generates an excel file:

as input my python method should take two excel files path the first one called small has the following columns:
|   |   |   |   |   |
|---|---|---|---|---|
|TYPE_DE_DEPOT|TYPE_DE_FICHIER|FINESS|NUMLOT|DATE_DE_TT|

and the second file called large has the following columns:
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|doc_date|doc_time|company_name|service_name|user_name|filiere|urgency|Nom du modele|Destinataire|numreco|statut|nb_pages|duree_archivage|Date depot poste|id_fichier|jobpath|ld_doc|nimmat|filler_01|filler_02|filler_03|filler_04|filler_05|latest_date|IdMailPiece|IdJob|

I want to join the tables on the following conditions:
filler_03=DATE_DE_TT these are date soo make sure to cast them as such to compare them
nimmat=NUMLOT
filler_05=FINESS

and I want to filter the result so that all the selected rows must verify:
TYPE_DE_DEPOT has value "type2"

then the results should be processed to be displayed in an excel file called "rapport delta currentdate" with the following columns and cell values:
+---------------+---------------------+---------------------+-------+
| DATE DE DEPOT | TOTAL GENERE/DEPOSE | TOTAL RAPPORT type2 | DELTA |
+---------------+---------------------+---------------------+-------+
| x             | y                   | z                   | =y-z   |
+---------------+---------------------+---------------------+-------+

where x y and z are placeholder values and there can be a lot of rows which are the result of the join and filtering of the input files

x should be the current date
y should be the count of rows with the value "type2" in the column TYPE_DE_DEPOT of the small input files
z should be the count of rows in the result of the joining and filtering explained above



==================================

now I want to update the code so that instead of creating an excel file every ttime, it only creates it if it doesn't exist yet and if it exists it just adds a row for the current date if it doesn't exist and if the row exists it updates it

venv\Scripts\activate

========================

now for NUMLOT and nimmat we should use a string and not a number and always have 3 characters, if there's less we need to ask zeros at the begining

for filler_05 and FINESS we should also always take it as a string. If there's 9 or more characters then do nothing else. If there's less than 9 characters we need to add zeros at he beginning until there's 9.

==========================

maintenant je veux que DATE DE DEPOT soit la date de création (dans les métadonnées du fichier) du fichier small