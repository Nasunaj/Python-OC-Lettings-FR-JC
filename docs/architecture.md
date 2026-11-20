# Architecture

## Overview

Django project structured into 3 applications:

- `oc_lettings_site`: root application (home page only)
- `lettings`: rental listings management (`Address` and `Letting` models)
- `profiles`: user profiles management (`Profile` model)

## Applications

| App | Models | Views | URLs (namespace) |
|---|---|---|---|
| oc_lettings_site | — | index | `/` |
| lettings | Address, Letting | index, letting | `lettings:index`, `lettings:letting` |
| profiles | Profile | index, profile | `profiles:index`, `profiles:profile` |

## Templates

- `templates/base.html`: shared layout (navbar, footer)
- Custom error pages: `templates/404.html`, `templates/500.html`
- Each app keeps its templates in `<app>/templates/<app>/`

## Key points

- Data from the former monolithic site was migrated to the new apps
  through Django `RunPython` data migrations (no raw SQL).
- `verbose_name_plural` set on `Address` ("Addresses").
- Docstrings on every module, class and function (basis for the
  Sphinx documentation).