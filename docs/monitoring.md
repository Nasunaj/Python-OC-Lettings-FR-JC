# Monitoring

Error tracking and logging for the OC Lettings application, based on Sentry.

## Overview

- **SDK**: `sentry-sdk==2.19.2`, pinned in `requirements.txt`
  (compatible with Python 3.8 and Django 3.0).
- **Integrations**: `DjangoIntegration` (unhandled exceptions in views,
  middleware and templates) and `LoggingIntegration` (bridges the standard
  Python `logging` module to Sentry).
- **Sensitive data**: the Django `SECRET_KEY` and the `SENTRY_DSN` are read
  from environment variables and never committed (see `.env.example`).

## Sentry project setup

1. Create a (free) account on [sentry.io](https://sentry.io).
2. Create a project: **Settings → Projects → Create Project → Django**.
3. Copy the DSN (Client Key)
   from **Settings → Projects → `<project>` → Client Keys (DSN)**.
   It looks like:
   `https://<key>@o<org>.ingest.sentry.io/<project>`.

## Application configuration

1. Copy `.env.example` to `.env` and fill in the values:

   ```text
   SECRET_KEY=<your-django-secret-key>
   SENTRY_DSN=<your-sentry-dsn>
   ```

2. On startup, `settings.py` loads `.env` with `python-dotenv`. If
   `SENTRY_DSN` is empty, Sentry is disabled: the application runs normally
   (useful for CI or local development without a Sentry account).
3. `sentry_sdk.init` is called early in `settings.py` with `DjangoIntegration`
   and `LoggingIntegration`. `send_default_pii=False` keeps personally
   identifiable information out of sent events (GDPR).

## Logging design

| Situation | Level | Console | Sentry |
|---|---|---|---|
| Normal page rendering (views) | INFO | yes | breadcrumbs only |
| Letting or profile not found | WARNING | yes | breadcrumbs only |
| Unknown URL | — | no app log | no event |
| Unhandled exception in a view | ERROR | yes (`django.request`) | event with traceback |

Key points, configured in `LOGGING` (settings.py):

- The root logger (`""`) sends every application message at INFO level or
  above to the console: each module uses `logging.getLogger(__name__)`
  and inherits from it.
- `django.request` logs unhandled view exceptions at ERROR level with
  `propagate: False` to avoid duplicate messages.
- `LoggingIntegration(level=INFO, event_level=ERROR)`: INFO messages are
  recorded as breadcrumbs, ERROR messages and above are sent to Sentry
  as standalone events.
- 404 pages for missing objects are logged WARNING (not sent as Sentry
  events): expected client errors are not application bugs.

Log messages use lazy `%s` formatting so Sentry groups identical issues
under one template.

## Verifying the pipeline

1. Run the application with a valid `SENTRY_DSN`:

   ```bash
   python manage.py runserver
   ```

2. Browse pages: `{asctime} INFO lettings.views ...` lines appear in the
   console.
3. Visit `/lettings/999/` (non-existing letting): a WARNING is logged and
   the custom 404 page is displayed.
4. During development, the SDK was verified by raising a deliberate
   `ZeroDivisionError` in a temporary `/debug-sentry/` view (removed
   afterwards). The event appeared in the Sentry dashboard with its full
   traceback, tags and breadcrumbs.
5. The automated test suite locks the behaviour in: INFO logging per view,
   404 + WARNING on missing objects (see `Test*Views` in each app tests,
   using the pytest `caplog` fixture).