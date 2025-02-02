# Utilisation d'une image Python de base
FROM python:3.12-slim

# Installation des outils de base nécessaires pour certaines bibliothèques comme psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application dans le conteneur
COPY . .

# Exposer le port utilisé par l'application
EXPOSE 8000

# Commande de lancement de l'application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "olympics_ticketing.wsgi:application"]

