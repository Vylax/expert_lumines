---

# 📝 **Rapport Hebdomadaire d'Équipe**  
**Période : [Semaine du xx/xx/2025 au xx/xx/2025]**  
**Équipe : [Nom de l’équipe]**

---

## 1. Points Bloquants et Difficultés Rencontrées

### Difficultés Rencontrées
- **RC PROTH** : Blocage lié à la **récupération incomplète des décomptes** par le robot, empêchant certaines relances.
- **Correspondances Payeurs/Concentrateurs** : Difficulté à relier certaines données, retardant les relances sans adresse mail.
- **TESSI** : Problème persistant sur la **génération des lots**. Des diagnostics ont été menés mais certaines anomalies restent ouvertes.
- **SICORFE** : **Package FSE** à réparer pour finaliser le rattrapage complet.

### Actions Déjà Entreprises
- Analyse des erreurs de génération de lots (TESSI).
- Mise en place d’un **suivi technique** sur les relances TP.
- Documentation de l’intégration SYLAE avec processus de validation.
- Débogage avancé sur les packages SSIS (SICORFE).
- Mise en place de contrôles sur les intégrations SYLAE pour fiabiliser le process + documentation étendue.

### Besoins en Soutien ou Ressources
- Support de l’équipe robot pour améliorer la transmission des décomptes manquants.
- Accès ou mise à jour d’un **fichier Excel CPAM** à jour pour aider au debug TESSI.

---

## 2. Projets et Tâches en Cours

| Projet / Tâche | Description | Avancement | Lien |
|---|---|---|---|
| RC SOIN | Relances mail (avec et sans adresse mail) | ✅ Terminé | [Lien Azure DevOps] |
| RC PROTH | Relances mail (avec et sans adresse mail) | ⏳ En cours - 60% | [Lien Azure DevOps] |
| SYLAE | Automatisation intégration + contrôle erreurs | ⏳ Passage en prod en cours | [Lien Azure DevOps](https://dev.azure.com/Dentego/Optimus/_git/Sylae_integration) |
| SICORFE | Débogage et rattrapage lot FSE | ⏳ En cours | [Lien Azure DevOps] |
| TESSI | Diagnostic et debug génération lots | ⏳ En cours - attente données | [Lien Azure DevOps](https://dev.azure.com/Dentego/Lumines/_git/TESSI%20-%20rapport%20delta%20automatique) |

N.B.: j'ai pas mis les liens devops pour la plupart pour l'instant mais je me dis que ce format pourrait être très pratique? A toi de me dire.

### Focus Antoine
- Relances TP (RC SOIN : terminé / RC PROTH : en cours).
- Suivi des décomptes robot.
- Suivi table et trigger de suivi des jobs.

### Focus Jordan
- Débogage et mise en production **SYLAE**.
- Suivi complet **SICORFE** (packages SSIS, rattrapages, validés avec Aisha).
- Coordination globale avec DevOps pour aligner les priorités (SYLAE, SICORFE, TESSI, Relances TP).
- TESSI debug + outils de diagnostics

---

## 3. Plan d’Action pour la Semaine à Venir

| Priorité | Actions Planifiées | Responsable |
|---|---|---|
| 🔴 Haute | Poursuivre le debug et les échanges avec TESSI pour les lots en erreur | Jordan |
| 🔴 Haute | Finaliser les relances RC PROTH | Antoine |
| 🔴 Haute | Passage de l’intégration SYLAE en production | Jordan |
| 🟠 Moyenne | Assurer le suivi des décomptes robot et relances avec complétude | Antoine |
| 🟠 Moyenne | Voir avec Aicha le probleme d'integration du rattrapage SICORFE dans le DAT | Jordan |
| 🟠 Moyenne | Préparer un bilan global des relances TP (SOINS + PROTH) | Antoine |
| 🟠 Moyenne | Réparer le **package FSE** de SICORFE et lancer le 2ème rattrapage | Jordan |
| 🟢 Basse | Documenter les points de blocage rencontrés avec TESSI  | Jordan |
| 🟢 Basse | TESSI Rapport automatique avec une vue globale  | Jordan |

---

## 4. Commentaires et Suggestions

### Observations
- 📌 Bonne coordination interne entre Antoine et Jordan sur les relances TP.
- 📌 Documentation process SYLAE validée, ce qui facilitera la maintenance future.
- 📌 Les échanges avec Aisha et Jessie fluidifient la validation des étapes techniques.

### Propositions d’Amélioration
- 🔄 Mettre en place un **tableau de bord de suivi multi-projets** pour visualiser en temps réel l’état d’avancement (Azure DevOps ou Power BI simple).
- 🔄 Automatiser un **rapport de complétude décomptes** côté robot avant chaque vague de relance pour éviter les interruptions en cours de traitement.
- 🔄 Anticiper une **revue globale des flux TESSI** pour identifier les zones critiques et préparer une roadmap de stabilisation.

### Retour sur les Outils et Process
- ✅ Azure DevOps est bien utilisé mais pourrait bénéficier d’une structuration plus claire des **lots de tâches liés** (ex. un Epic par processus complet : relances TP, SYLAE, etc.).
- ✅ Besoin d’un **référentiel centralisé** pour les correspondances CPAM et Concentrateurs, facilement accessible par tous.

---

Veux-tu un export format Word ou un template prêt pour les prochaines semaines ? 😊