# Run

## Docker
`docker-compose up`

## Manual
```
virtualenv .env --no-site-packages -p python3
source .env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

# API

## Entry point
`http://127.0.0.1:8000/api/`

### Create admin
`docker exec -it api python manage.py createsuperuser`
