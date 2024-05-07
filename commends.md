# Packages

Django==4.2
python-dotenv==1.0.1
djangorestframework==3.14.0
pytest==8.2.0
pytest-django==4.8.0
black==24.4.2
flake8==7.0.0

# Commands

./venv/Scripts/activate

django-admin startproject drf_ecommerce

cd drf_ecommerce

pip install -r reqiurements.txt

py manage.py makemigrations

py manage.py migrate

py manage.py createsuperuser

py manage.py runserver
