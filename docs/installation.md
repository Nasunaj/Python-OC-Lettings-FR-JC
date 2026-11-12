# Installation

## Prérequis

- Python 3.8 ou supérieur
- Git
- SQLite3

## Installation

- Cloner le repository :
  `git clone https://github.com/Nasunaj/Python-OC-Lettings-FR-JC.git`
- Créer et activer l'environnement virtuel :
  `python -m venv venv`
  `source venv/bin/activate` (Linux/Mac) ou `.\\venv\\Scripts\\Activate.ps1` (Windows)
- Installer les dépendances :
  `pip install -r requirements.txt`
- Appliquer les migrations :
  `python manage.py migrate`

## Lancer le site

- `python manage.py runserver`
- Ouvrir `http://localhost:8000`

## Panel d'administration

- Ouvrir `http://localhost:8000/admin`
- Utilisateur : `admin` / Mot de passe : `Abc1234!`