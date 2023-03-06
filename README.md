# online-school

1) Download all the libraries and packages with the required versions required for the project using the command:

```
pip install -r requirements.txt
```

2) We start docker, thereby creating a local database using the command:

```
docker-compose up -d
```

3) Create a migrations

```
python manage.py makemigrations
```

4) Synchronizing migrations using the command:

```
python manage.py migrate
```

5) Create a superuser for administration using the command:

```
python manage.py createsuperuser 
```

6) Run the application locally using the command:

```
python manage.py runserver
```

