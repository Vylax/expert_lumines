veasy_recup_data_et_maj_iddoc_fds.dtsx

à la sortie du trie fusionner les données
	utiliser un bloc Unir tout
		cf: [ressource1](https://learn.microsoft.com/fr-fr/sql/integration-services/data-flow/transformations/union-all-transformation?view=sql-server-ver16&f1url=%3FappId%3DDev15IDEF1%26l%3Dfr-FR%26k%3Dk(sql13.dts.designer.unionalltrans.f1)%26rd%3Dtrue)
		cf: [ressource2](https://learn.microsoft.com/fr-fr/sql/integration-services/data-flow/transformations/merge-data-by-using-the-union-all-transformation?view=sql-server-ver16)


idée: via script cs:
supprimer l'ancien bloc de tri
- avant que les rows passent à travers le script:
	- initialiser la liste
- après ////////:
	- trier la liste comme dans le bloc tri
	- appeller GenererFSEViaApiAsync pour chaque row
