# Projet_9

## Les différents dossiers :
Dossier Projet : contient les différents programmes réalisés durant la durée du projet.
Dossier Soutenance : contient les différents éléments présenter durant la soutenance.
Dossier Tuto : contient les différents exemples réalisés par notre intervenant.

### Détails du dossier Soutenance :
Ce dossier contient :
- Le programme de scrapping du site de la centrale en python, nommée Scrapping.py.
- Deux exemples de résultats de scrapping sous la forme de fichier csv :
  - "data_5_pages" : le résultat de 5 pages scrapper.
  - "data_10_pages" : le résultat de 10 pages scrapper.

#### Utilisation de Scrapping.py :
Vous avez juste à lancer le programme pour obtenir un nouveau fichier csv avec les résulats du scrapping.

Vous pouvez modifier les paramètres suivant :
- Dans la fonction main :
  - brand_name = 'PEUGEOT' ; Remplacer 'PEUGEOT' par n'importe quelle autre marque disponible sur la centrale.
  - while page_number <= 5 ; Remplacer la valeur '5' par le nombre de pages que vous souhaitez scrapper. Si vous mettez un nombre supérieur de pages à scrapper par rapport aux nombres de pages disponible sur la centrale, le programme fonctionnera quand même.

- Dans la fonction url :
  - Vous pouvez modifier les différents paramètres de recherches. 
