- indus: antoines
- TP à faire

le sfichiers sont deposer sur le FTP par sicorfe mais ne sont pas charger correctement

-> soucis de format
	-> mapping casser
			-> package casser
metadata introuvable

cf message teams

DEB: debit et rejet
FSE: liste des paiements effectués par siccorfe du mardi precedent au mardi de cette semaine
MAJ cote lumine des rejet et paiements

package executer tt les lundis a 2h du mat

package ko depuis ???

tt les packages sont ds integrations service catalogue puis ds le sous dossier defini au deploiement

sous dossier: SICORFE
premier step execute le package SIC - FICHIERS DE DEBIT NEW

sur le job: clic droit propriete, puis edit pour voir le chemin du package

click droit report old execution pour voir les historique d'execution du package


detaill de l'error: all message ou overview


moi:
lundi: surveillé s'il a encore des pb a s'execute: verifier lexecution et voir si les 3 etapes sont bien eecuté

niveau d'encryption: mdp
version: SQL server 2017
run64bit: false





Ce que j'ai fait:
25-02-17:
- changer les chemins du package de `\\Team-it\FICHIERS-TEAM-IT` vers `E:`
- cherche a changer le mdp de la connection ftp: besoin du mdp via Aisha