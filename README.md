# sample_ims

This is a sample application to manage an inventory.

## Requirements
- Python
- Django
- PostgreSQL

## Setup

Clone the repository:

```sh
$ https://github.com/anushajp/sample_ims.git
```

Create a virtual environment(python3) and activate it:

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Change the directory to project directory and run the server

```sn
(env)$ cd sample_ims
(env)$ python manage.py runserver --settings=sample_ims.settings.dev
```
And navigate to `http://127.0.0.1:8000`.

Run migrations

```sn
(env)$ python manage.py migrate --settings=sample_ims.settings.dev
```
Create superuser

```sn
(env)$ python manage.py createsuperuser --settings=sample_ims.settings.dev
```

