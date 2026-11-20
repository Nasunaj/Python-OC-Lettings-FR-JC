Quality
=======

Linting
-------

- Tool: flake8 (configuration in ``setup.cfg``, ``max-line-length = 99``)
- Command: ``flake8``
- Status: 0 error

Tests
-----

- Tools: pytest, pytest-django
- Tests live in each app: ``lettings/tests.py``, ``profiles/tests.py``,
  ``oc_lettings_site/tests.py``
- Command: ``pytest``
- Status: 24 tests, all passing (models, views, URLs, logging behaviour)

Coverage
--------

- Tool: pytest-cov (exclusions in ``setup.cfg``, ``[coverage:run]`` section)
- Command: ``pytest --cov=. --cov-report=term-missing``
- Status: 93% total coverage (brief requirement: > 80%)
- All application modules (models, views, URLs, admin) are covered at 100%;
  only the ASGI/WSGI entry points and one settings line remain uncovered
- Exclusions: migrations, test files, apps.py, manage.py

Commit convention
-----------------

Conventional format: ``Feat:``, ``Fix:``, ``Docs:``, ``Test:``, ``Chore:``
