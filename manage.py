"""
Command-line utility for administrative tasks of the oc_lettings_site project.
"""

import os
import sys


def main():
    """
    Run administrative tasks of the Django project.

    Sets the DJANGO_SETTINGS_MODULE environment variable and executes
    the command passed as the first command-line argument.

    Raises:
        CommandError: if the command execution fails.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
