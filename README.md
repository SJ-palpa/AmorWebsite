# A.M.OR Platform

[![Python version](https://badgen.net/badge/Python/3.4.x/green)] (https://www.python.org/)

## How to dev and run the platform locally

### On a Mac/linux System

* Install Python 3.4.3 or higher (if higher, please test your code on 3.4.3)
* Install PostgresSQL
* Create a database

* install pip:
https://www.liquidweb.com/kb/install-pip-windows/

* Root of the project
* Create a virtual environnement

virtualenv -p python3 venv

* Root of the project
* Activate venv:

workon venv

* install packages

pip install -r requirements.txt

* AmorWebsite/settings.py
* In settings.py modify:
username
password
Host mettre Localhost
Port enlever la ligne

exemple:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'amor-platform',
        'USER': 'amor-platform',
        'PASSWORD': '#######',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            # Tell postgresSQL to connect with 'utf8mb4' character set
            'charset': 'utf8mb4',
    },
  }
}

* Finally run this command:
python manage.py runserver
