
- Pas avancé:
	- Documentation LUMINES  
	  - code LUMINES récupéré, mis sur le repos + dockerisé avec [@Jessie UGOLIN](mailto:jessie.ugolin@dentego.fr) 
		  - @Antoine continue d'élargir la part du code mis en repo
	  - doc fonctionnelle/utilisateur reçu, mais clairement pas suffisante  
	  - Nécessite tjrs le transfert de compétence de [@Aicha Diakité](mailto:aicha.diakite@dentego.fr) afin de pouvoir cartographier les process de LUMINES et documenter
	- [x] En attente du code de [@Aicha Diakité](mailto:aicha.diakite@dentego.fr)  
	- [ ] Fix SICOREFE issue avec [@Antoine ZAMORD](mailto:antoine.zamord@dentego.fr) en attente, la priorité actuelle d'antoine reste sur la relance TP mail
	- P3 TEULADES  
		  - nécessite également le transfert de compétence de [@Aicha Diakité](mailto:aicha.diakite@dentego.fr) sur LUMINES  

- Avancé:
	- P1 : SUBVENTION = SYLAE  
		  - Le robot est completement cassé, du coup @Aisha reprends et compte le finir d'ici Lundi
		  - Pour la partie intégration je continue de bosser sur l'automation, des contraintes se sont rajoutés (recuperation FTP et contrainte sur l'intégration en BDD), et ils reste les tests et mettre la docu en forme pour la maintenance. Je fini la partie intégration d'ici mardi soir.
	- P1 : SICORFE
		- Package réparé et executé, sera deployer d'ici Lundi soir et pour les rattrapage on est en attente de SICORFE (relancés par @Aisha)
	- Problème TESSI  
	  - ~~Script fonctionnel MAIS :~~  
		- ~~manque l'automation du traitement de donnée~~  
			- La donnée est recoltée automatiquement depuis les mails et mis à jour
			- On pourrait faire en sorte que ce reporting soit fait tt les matins à 9h15 et nous soit envoyer par mail mais je dois voir avec antoine pour ca
		- manque l'indicateur de ce qui a été rempli à la main 
		- on va suivre ca sur les jours qui suivent pour voir si le script ne loupe rien
Pour une version plus détaillé des taches effectués cf après le rapport d'antoine
### Détail des tâches effectuées cette semaine :  

#### **SICORFE**  
- Réparation du job qui n’a pas tourné :
  - Formation SSIS en autonome (manque de transmission des competences)
  - Actualisation des chemins dans les variables et paramètres (SSMS & SSIS).  
  - Résolution du problème de connexion FTP (mise à jour du mot de passe).
	- Récuperer les mot de passes (j'ai du déchiffrer les données de filezilla pour obtenir l'information --> On devrait pouvoir trouver l'information sans avoir recours à ca)
  - Investigation sur l'absence de fichiers sur le FTP (possibilité de changement de convention ou problème côté Sicorfe).  
- Consultation avec Antoine pour avancer sur le problème.  
- Installation du connecteur DB. (L'information a ete TRES compliqué à obtenir, on devrait documenter et archiver les packages utilisés dans le cas ou MS decide de supprimer les lien de DL et Aisha ne devrait pas etre la seule à avoir l'information de quels packages sont utilise) 
- Debug et tests du package.  
- Remise des chemins en `E:` pour déploiement.  

#### **SYLAE**  
- Correction et amélioration du robot :  
  - Vérification de la présence de la liste de Finess.
  - Travail sur UIPath pour Sylaé. Formation en autonomie.
  - Debug du robot (bloqué sur un élément Click).  
- Travail sur le script de consolidation des fichiers Excel traités.  
  - Récupération des fichiers template.  
  - Définition des étapes de traitement des données.  
  - Mise en place du script ETL (testé, mais avec conflit sur contrainte de clé étrangère `id_decompte`).  
  - Ajout de la partie FTP à l’intégration Sylaé.  
  - Amélioration de la requête avec `IF NOT EXISTS`.  
  - Probleme d'insertion des logs dans `LOGDECOMPTE`.  
  - Tests commencé avec différents cas (export vide/plein, erreurs).  

#### **Autres tâches**  
- Réunions et mises à jour :  
  - Réunion et rapports pour Tessi.  
  - Rapport en automatique opérationnel
  - Mise à jour d’équipe avec Jessie.  
- Gestion des problèmes techniques :  
  - Problèmes de déploiement et de Git avec Antoine.  
  - Passation de sujets en maintenance avec Antoine.  (a revoir comme mentionné au dessus)
- Matinée passée sur site (20e)

Je reste à ta disposition pour toute question.


### **Estimation de fin des tâches pour SYLAE et SICORFE**
- **SYLAE**
    - **Robot** : Aisha prévoit de le finaliser **d’ici lundi**.
    - **Intégration** : Les derniers ajustements (récupération FTP, contrainte en BDD, tests, documentation) seront terminés **d’ici mardi soir**.
- **SICORFE**
    - **Package réparé et exécuté**.
    - **Déploiement prévu pour lundi soir**.
    - **Rattrapage des données en attente de SICORFE**, Aisha a relancé.

Si tout se passe comme prévu, **SYLAE sera terminé mardi soir** et **SICORFE lundi soir, en attendant la réponse de SICORFE pour les rattrapages**.