release: python SRS/manage.py migrate
web: gunicorn --pythonpath SRS SRS.wsgi --log-file -
