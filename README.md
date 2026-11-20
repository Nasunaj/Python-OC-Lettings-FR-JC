# OC Lettings 2.0

Orange County Lettings web application - OpenClassrooms refactoring project.
Django web app listing holiday rental properties and user profiles.

[![CI](https://github.com/Nasunaj/Python-OC-Lettings-FR-JC/actions/workflows/ci.yml/badge.svg)](https://github.com/Nasunaj/Python-OC-Lettings-FR-JC/actions/workflows/ci.yml)

## Links

- Live application: https://oc-lettings-zjlv.onrender.com
- Docker image: https://hub.docker.com/r/nasunaj/oc-lettings
- CI pipeline: https://github.com/Nasunaj/Python-OC-Lettings-FR-JC/actions

[![Documentation Status](https://readthedocs.org/projects/oc-lettings-jc/badge/?version=latest)](https://oc-lettings-jc.readthedocs.io/en/latest/)

## Documentation

Full documentation is published on Read the Docs: https://oc-lettings-jc.readthedocs.io/

- [Installation](https://oc-lettings-jc.readthedocs.io/en/latest/installation/)
- [Architecture](https://oc-lettings-jc.readthedocs.io/en/latest/architecture/)
- [Quality](https://oc-lettings-jc.readthedocs.io/en/latest/quality/)
- [Monitoring](https://oc-lettings-jc.readthedocs.io/en/latest/monitoring/)
- [Deployment](https://oc-lettings-jc.readthedocs.io/en/latest/deployment/)
- [API reference](https://oc-lettings-jc.readthedocs.io/en/latest/api/lettings/)

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
