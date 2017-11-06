# Les votes par sms du Louvain-li-nux

Salut a toi, jeune padawan ! Si tu est pressé, regarde la section "vite steu plé" pour tout mettre en place en 3 minutes. SI tu a le temps ou que tout est cassé, regarde après.

## Infos utils

- Numéro des votes: 0499/40.93.44
- Format des votes: 
	`<préfix>` `<entrée>` 
	Exemple: folklo 14
- Le préfix et les votes doivent être en un mot, sans accents et uniquement avec les caractères suivants: [a-zA-Z0-9]

## Vite steu plé

1. Va chercher la pi dans la chanbre patrimoine, la carte sd du py et la clef usb sim (a carte sim du linux est dedans).
2. Met la carte SD dans le pi.
3. Branche la clef usb au pi.
4. Branche en Ethernet le pi au deuxième routeur dans le commu.
5. Branche le pi a un des routers pour l'alimenter
6. Depuis le réseau `louvain-li-nux` ou en filliaire sur le deuxième réseau du kot, connecte toi en ssh sur cette ip: 192.168.2.12; avec l'utilisateur `tuxvote` et le mot de passe `minituxvote`
7. Va dans la dossier `SMS-vote` et édite la fichier config.py
8. Si tu veux effacer tout les aciens sondages, remplace l'entrée vote par ceci: `vote = []`
9. Pour ajouter un sondage, ajoute une entrée comme ceci: `{"prefix"="tonPrefix", "filtered":filtre, "allowedEntry":["Entrée 1","Entrée 2","Entrée 3","..."]}` en remplacant tonPrefix par ce que tu veux, mettant filtre a true si tu veux limiter les possibilité et liste dans allowedEntry les entrée autorisée. Par exemple, pour le vote folklo des 24, la ligne resemblait à ca: 

`vote = [
        {"prefix" : "folklo", "filtered": True, "allowedEntry": ["1","4","6","8","9","11","12","13","14","15","16","17","18","20","21","22","25","27","28","30","31","32","33","34","36","37","39","42","43","45","50","53","57","59","61","62","64","66","67","68","70","71","74"]}
        ]`

10. Exécute `./createConstest.py out` et prend note de l'url des résultats.
11. Fini !

