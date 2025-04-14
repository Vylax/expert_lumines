#ssis #guide 
## Problèmes fréquents:

### WinSCP :
Une erreur est levée lorsque vous exécutez un package faisant appel à WinSCP dans un composant script -> la référence est manquante au runtime, meme si elle est correctement configurée dans votre composant.

Fix: Pour fonctionner avec SSIS, WinSCP doit être inscrit dans la Global Assembly Cache (ou GAC) de votre machine.

1. Vérifiez que "gacutil.exe" est bien présent sur votre machine. Typiquement localisé ici: `C:\Program Files (x86)\Microsoft SDKs\Windows\v10.0A\bin\NETFX 4.8 Tools\gacutil.exe`.

>[!tip] Conseil: 
>Everything de voidtools vous permet de rapidement localiser n'importe quel fichier sur votre machine 😉
>

2. Dans votre ligne de commande **en mode administrateur**, utilisez gacutil pour référencer WinSCP:
```bash
gacutil -i "CHEMIN\WinSCPnet.dll"
```

Si gacutil n'est pas une commande reconnue, essayez de lancer la commande en pointant directement vers le .exe:
```bash
"C:\Program Files (x86)\Microsoft SDKs\Windows\v10.0A\bin\NETFX 4.8 Tools\gacutil.exe" -i "path\to\WinSCPnet.dll"
```

*Source:(https://winscp.net/eng/docs/message_net_system_cannot_find_file_specified)*

-------------------------------------

### Microsoft ACE.OLEDB (Access Database Engine) :
Pour la manipulation de fichiers Excel dans SSIS, vous pouvez rencontrer une erreur comme quoi le pilote Microsoft ACE est introuvable sur votre machine.

A priori, seule la version 32bit de ce pilote fonctionne. Si vous tentez de l'installer, vous aurez surement une erreur à l'installation à cause d'un module Office incompatible.

Pour désinstaller ce module: 

1. Windows + R ; entrez: "installer" ; OK
2. Dans la fenêtre de l'explorateur windows: affichez la colonne "Object" (ou Subject en Anglais)
3. Triez puis scrollez jusqu'à trouver: Office 16 Extensibility Module.msi (nom inexact dans cette doc)
4. Clic droit + désinstaller 

*À l'heure de l'écriture de ce guide, retirer ce module n'a créé aucun problème dans mon utilisation de la suite Office.*

-----------------------------------------
