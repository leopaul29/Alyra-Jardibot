# Alyra Jardibot

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

### import solo

pip install "fastapi[standard]"
pip install pandas
pip install tensorflow==2.18
pip install Pillow

## run le backend endpoint

fastapi dev .\app\main.py

- serveur: http://localhost:8000/
- swagger: http://localhost:8000/docs
