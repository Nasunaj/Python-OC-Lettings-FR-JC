# Qualité

## Linting

- Outil : flake8 (config dans `setup.cfg`, `max-line-length = 99`)
- Commande : `flake8`
- Statut : 0 erreur (étape 2 terminée)

## Tests

- Outils : pytest, pytest-django
- Tests placés dans chaque app : `lettings/tests.py`, `profiles/tests.py`,
  `oc_lettings_site/tests.py`
- Commande : `pytest`

## Couverture

- Outil : pytest-cov (exclusions dans `setup.cfg`, section `[coverage:run]`)
- Commande : `pytest --cov=. --cov-report=term-missing`
- Statut : 20 tests, 92 % de couverture (critère du brief : > 80 %)
- Exclusions : migrations, fichiers de test, apps.py, manage.py

## Convention des commits

Format conventional : `Feat:`, `Fix:`, `Docs:`, `Test:`, `Chore:`