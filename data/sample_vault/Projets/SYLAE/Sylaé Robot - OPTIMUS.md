Yossi adrien: lot 1
hugo lot 2

recupération de décompte syllae: historique de paiement

sylae: subvention pour le salternants
par trimestre pour chaques alternants

3 acces au portail:
- sur chaque acces on retrouve des groupes diff qui contiennent des sous-centres
- pour chaque siret consulter les historique d'avis de paiements
- 3eme acces: une etape en moins: 1 seule societe selectionné par defaut donc 1 etape a sauter
	- un if a faire: un check app state: verifier le status
		- equiv a DOM ready
			- utiliser la reconnaissance html: se baser sur le DOM

robot sur la `VM-ROBOT-5`

2eme chose a faire :
- ajouter le RE framewrok au dev robot

RE framework: nouveau robot : infrastructure d'entreprise robotique

vaariable rattrapage

moi:
- mettre log: composant log message
- relance pour ne pas recommencer du debut a chaque fois: ignore les trucs deja traités

apres le robot partie ETL:
- table a remplir avec les lignes de chaques fichiers: dbo.OPTIMUS_SYLAE_PAIEMENTS id_decompte=nom du fichier
- repertoire des fichiers excel apres avoir tourné le robot: C:\Users\OrchestratorUiPath\Documents\UiPath\LOT_12_SYLAE_PAIEMENTS\Excel Paiement Sylae
[[SYLAE ETL]]
