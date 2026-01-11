# Late Show API

A Flask API for tracking Late Show episodes, guests, and their appearances.

## Setup

- `pipenv install flask flask_sqlalchemy flask_migrate sqlalchemy-serializer`

- `pipenv shell`

## Database

- `flask db init`
- `flask db migrate -m"create tables"`
- `flask db upgrade`
- `python seed.py`

