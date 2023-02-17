#### DJASONvgame
CREAR PROYECTO EN DJANGO
#### Paso 1
Crear un directorio – mkdir <nombre directorio>
#### Paso 2
Crear un ambiente – Python -m venv  <nombre del ambiente>
#### Paso 3 
Activar el ambiente – correr activate
#### Paso 4 
Instalar librerías base: 
pip install djangorestframework
pip freeze (ver versiones)
#### Paso 5
Crear proyecto: django-admin startproject <proyecto>
#### Paso 6
Ejecutar proyecto Django: 
python manage.py runserver
#### Paso 7 
Crear base de datos Django:
python manage.py migrate
#### Paso 8
Crear aplicación:
Python manage.py startapp <nombre app>
#### Paso 9
Configurar apps en settings.py:
INSTALLED APPS 
‘rest_framework’, ‘api’
#### Paso 10
Crear clase en models.py
#### Paso 11
Crear migraciones a la base de datos
Python manage.py makemigrations
Python manage.py migrate
