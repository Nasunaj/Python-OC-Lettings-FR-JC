# Base image: Python 3.8 as required by the project brief.
FROM python:3.8-slim

# Do not buffer Python output: logs appear immediately in docker logs.
ENV PYTHONUNBUFFERED=1
# Do not write .pyc files (useless in a container).
ENV PYTHONDONTWRITEBYTECODE=1

# Install dependencies first to leverage Docker's layer cache:
# this layer is rebuilt only when requirements.txt changes.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code and the SQLite database into the image.
COPY . .

# Collect static files inside the image in PRODUCTION mode (DEBUG=False):
# this generates the WhiteNoise manifest (staticfiles.json) that the
# runtime expects, since the container also runs with DEBUG=False.
RUN SECRET_KEY=docker-build-placeholder DEBUG=False python manage.py collectstatic --noinput

# Port used by gunicorn inside the container.
EXPOSE 8000

# Production server: gunicorn, listening on all interfaces so the
# container port is reachable from the outside.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]