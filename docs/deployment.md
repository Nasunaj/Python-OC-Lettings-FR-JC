# Deployment (CI/CD, Docker and Render)

## Overview / Architecture

Git push (main) → GitHub Actions CI → Docker image build → Docker Hub → Render deploy

## Branching model (Git Flow)

- `feature/*` → development and validation (lint + tests + coverage gate at each push)
- `develop` → integration branch, quality job only (Docker build/push skipped)
- `main` → production branch: quality job + Docker build & push
- All merges use `--no-ff` to keep the feature history readable

## CI pipeline (GitHub Actions, `.github/workflows/ci.yml`)

- Quality job (all branches): flake8, pytest (24 tests), coverage (92%)
- Docker job (`main` only): build + push two tags (`latest` + commit SHA)
- Secrets: `DOCKERHUB_USERNAME`, `DOCKERHUB_TOKEN` (GitHub Actions secrets,
  never committed)

## Docker image

- Base: `python:3.8-slim`, non-root user, gunicorn as CMD
- Multi-concern layers ordered for cache efficiency
- Static files collected in PRODUCTION mode during build (DEBUG=False):
  the WhiteNoise manifest is generated at build time, matching runtime
  conditions
- Ships the demo SQLite database (deliberate choice for this fictive
  project; in real production an external PostgreSQL would be mounted)

## Deployment (Render)

- Source: existing public image `docker.io/nasunaj/oc-lettings:latest`
  (deployed from the registry, NOT from Git: what runs in production is
  exactly the tested image, and no push can ever trigger a deploy)
- Auto-deploy: disabled — deploying is a manual, intentional act
- Environment: SECRET_KEY, DEBUG=False, ALLOWED_HOSTS, SENTRY_DSN
- Live URL: https://oc-lettings-zjlv.onrender.com

## End-to-end verification (final review test)

1. Change the home page title on a feature branch
2. Merge feature → develop → main (CI green at each step)
3. Manual deploy on Render → new title live
4. `docker pull nasunaj/oc-lettings:latest` → new title in the extracted image