# videoCMS
A perofetional CMS for video


#How to create a virtual enviroment
python -m virtualenv .venv
.\.venv\Scripts\activate
deactivate
pip install -r requirements.txt
pip freeze
django-admin startproject core . 
python manage.py migrate
python manage.py runserver
python manage.py startapp first_app
python manage.py makemigrations {app_name}
python manage.py shell
python manage.py shell -i ipython
python manage.py createsuperuser
pipenv install 