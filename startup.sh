# Start Gunicorn for Django
gunicorn backend.wsgi:application
 
# Start Daphne for ASGI
daphne backend.asgi:application

