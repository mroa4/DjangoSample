# DjangoSimple

## start

1. python3 -m venv env

2. source env/bin/activate

3. python -m pip install -r requirements.txt

    OR

    ```shell
    python -m pip install django
    python -m pip freeze > requirements.txt
    ```

4. django-admin startproject DjangoSimple .

5. python manage.py startapp ports

6. python manage.py migrate

7. add ports.apps.PortsConfig to installed

8. create db model for ports

9. python manage.py makemigrations ports

10. python manage.py sqlmigrate polls 0001 OR python manage.py migrate

11. add urls, views and templates

12. python manage.py createsuperuser

13. python manage.py runserver

14. add others
