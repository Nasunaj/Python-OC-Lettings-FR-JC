# OC Lettings 2.0

Orange County Lettings web application - OpenClassrooms refactoring project.
Django web app listing holiday rental properties and user profiles.

[![CI](https://github.com/Nasunaj/Python-OC-Lettings-FR-JC/actions/workflows/ci.yml/badge.svg)](https://github.com/Nasunaj/Python-OC-Lettings-FR-JC/actions/workflows/ci.yml)

## Links

- Live application: https://oc-lettings-zjlv.onrender.com
- Docker image: https://hub.docker.com/r/nasunaj/oc-lettings
- CI pipeline: https://github.com/Nasunaj/Python-OC-Lettings-FR-JC/actions

## Documentation

- [Installation](docs/installation.md)
- [Architecture](docs/architecture.md)
- [Qualité (lint, tests, couverture)](docs/quality.md)
- [Monitoring](docs/monitoring.md)
- [Deployment (CI/CD, Docker, Render)](docs/deployment.md)

## Quick start (local)

- `python -m venv venv && source venv/bin/activate`
- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py runserver`
- Open `http://localhost:8000`

## Quick start (Docker)

- `docker run --rm -d -p 8000:8000 -e DEBUG=False -e ALLOWED_HOSTS=localhost -e SECRET_KEY=<key> nasunaj/oc-lettings:latest`
- Open `http://localhost:8000`

## Accounts

- Django admin: `admin` / `Abc1234!` (demo credentials)
