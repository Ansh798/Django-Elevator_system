 # to install updated requirements
 echo Installing dependencies
 pip3 install -r requirements.txt
 # To rename app
 #python3 manage.py rename_app base renewbuy
 
 # Migrate
 echo Creating Migration files.
 python3 manage.py makemigrations
 echo Starting Migration.
 python3 manage.py migrate
 
 
 # Collect static files
 echo Collecting static files.
 python3 manage.py collectstatic --no-input

 
 # Start Gunicorn processes
 echo Starting Gunicorn.
 
 DJANGO_DIR=/elevator_system
 PYTHONPATH=$DJANGO_DIR:$PYTHONPATH
 export PYTHONPATH
 exec gunicorn elevator_system.wsgi:application \
     --bind 0.0.0.0:9000 \
     --workers 4 \
     --log-level=info \
     --timeout 120 \