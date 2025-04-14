Dans ma BDD j'ai une table dbo.TESTTABLE avec la structure suivante:
colonnes en db:
idPaiement: int PK
siret: varchar(200)
denomination: varchar(500)
date_de_paiement: varchar(50)
numero_de_dossier: varchar(200)
nom_du_salarie: varchar(500)
prenom_du_salarie: varchar(500)
mois_d_effet: varchar(200)
prestation: varchar(MAX)
montant_echeance: decimal(28, 2)
id_decompte: varchar(200) FK

j'ai plein de fichiers excels avec 2 pages, celle qui m'intéresse s'intitule "Détails par salarié" qui contient les colonnes suivantes: 
|SIRET|Dénomination|Date de paiement|Numéro de dossier|Nom du salarié|Prénom du salarié|Mois d'effet|Prestation|Montant échéance|

je veux un script python qui:
- créer un fichier excel qui contient toutes les lignes des pages qui m'intéresse de tous les fichiers excel dans un répertoire donné avec une colonne en plus a la fin (id_decompte) qui contient le nom du fichier excel d'ou vient cette ligne à l'origine
- puis dans un second temps met a jour ma table en y ajoutant toutes les lignes sans duplicata, sachant que idPaiement a un autoincrement

---

Met à jour le code de sorte que:
- Si un fichier est en erreur lors de l'étape 1, le fichier en question est déplacer vers le dossier de chemin erreurs_premerge
- A la fin de l'execution de l'étape 1, les fichiers qui ne sont pas en erreurs sont deplacer vers archive_input
- Si il y a une erreur sur une ligne lors de l'étape trois, on créer un fichier excel qui contient toutes les lignes en erreurs de l'étape 3 que l'on nomme selon la variable erreurs_postmerge
- A la fin de l'éxecution de chaque etape on a le pourcentage de reussite, le nombre de succes, le nombre d'echec et la valeur de date actuelle
- A la fin de l'execution le fichier merge est placer dans archive_merge
- On ajoute un parametre retry_erreurs boolean a true
- si retry_erreurs est true:
	- on prend tout les fichiers qui sont dans erreurs_premerge, et on les place dans input_directory avant de commencer l'étape 1
	- avant de finir l'etape 2, on greffe egalement au df toutes les lignes de tous les fichers dans erreurs_postmerge, une fois que l'etape 2 fini correctement, on supprime ces fichiers de erreurs_postmerge

1760
438