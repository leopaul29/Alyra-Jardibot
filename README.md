# Alyra Jardibot

Dans le cadre de la formation Alyra, ce projet contient 2 sous projets:

- projet1: machine learning
- projet2: deep learning + MlOPs

## lib

- pandas
- uvicorn
- fastapi
- tensorflow

## venv

init venv
`python -m venv venv`

activer la venv
`.\venv\Scripts\activate`

À chaque fois que vous installez une nouvelle bibliothèque avec pip install, vous pouvez régénérer ou mettre à jour votre requirements.txt en répétant la commande :
`pip freeze > requirements.txt`
Cela garantira que toutes les nouvelles dépendances ajoutées à votre projet sont correctement listées dans le fichier.

installer toutes les lib
`pip install -r requirements.txt`

desactiver la venv
`deactivate`

## run le backend endpoint

use the command line:

`fastapi dev .\app\main.py`

test live on urls:

- serveur: http://localhost:8000/
- swagger: http://localhost:8000/docs

```

```
