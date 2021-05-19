pip3 install -r requirements.txt
cp local_settings_example.py local_settings.py
echo "database processing !!!!!!!!"
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput
export DJANGO_SUPERUSER_USERNAME=ozhan
export DJANGO_SUPERUSER_EMAIL=ozhan@datametric.uk
export DJANGO_SUPERUSER_PASSWORD=Ozh456
python3 manage.py createsuperuser --noinput
python3 manage.py runserver 0.0.0.0:8000
tail -f /var/log/*.log
