web: gunicorn the_factory_bot.wsgi --log-file -
worker: python3 manage.py shell < bot/bot.py
release: python manage.py migrate