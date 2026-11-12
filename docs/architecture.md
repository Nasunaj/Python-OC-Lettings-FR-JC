# Architecture

## Vue d'ensemble

Projet Django structuré en 3 applications :

- `oc_lettings_site` : application racine (page d'accueil uniquement)
- `lettings` : gestion des locations (modèles `Address` et `Letting`)
- `profiles` : gestion des profils utilisateurs (modèle `Profile`)

## Applications

| App | Modèles | Vues | URLs (namespace) |
|---|---|---|---|
| oc_lettings_site | — | index | `/` |
| lettings | Address, Letting | index, letting | `lettings:index`, `lettings:letting` |
| profiles | Profile | index, profile | `profiles:index`, `profiles:profile` |

## Templates

- `templates/base.html` : layout partagé (navbar, footer)
- Templates d'erreurs personnalisés : `templates/404.html`, `templates/500.html`
- Chaque app a ses templates dans `<app>/templates/<app>/`

## Points clés

- Les données de l'ancien site monolithique ont été migrées vers les
  nouvelles apps via des migrations Django `RunPython` (pas de SQL brut)
- `verbose_name_plural` définit sur `Address` ("Addresses")
- Docstrings sur chaque module, classe et fonction (base de la
  documentation Sphinx de l'étape 5)