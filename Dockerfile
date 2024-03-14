FROM python:3.9-slim

WORKDIR /app

# requirements.txt généré avec : pip freeze > requirements.txt
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# Commande de lancement de l'app Flask
CMD ["python", "main.py"]