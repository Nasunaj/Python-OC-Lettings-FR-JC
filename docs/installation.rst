Installation
============

Prerequisites
-------------

- Python 3.8 or later
- Git
- SQLite3

Setup
-----

Clone the repository:

.. code-block:: bash

   git clone https://github.com/Nasunaj/Python-OC-Lettings-FR-JC.git

Create and activate a virtual environment:

.. code-block:: bash

   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\Activate.ps1  # Windows

Install dependencies:

.. code-block:: bash

   pip install -r requirements.txt

Apply migrations:

.. code-block:: bash

   python manage.py migrate

Run the site
------------

.. code-block:: bash

   python manage.py runserver

Open ``http://localhost:8000``.

Admin panel
-----------

Open ``http://localhost:8000/admin``.

- User: ``admin``
- Password: ``Abc1234!``
