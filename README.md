# rfid-tag-django-api
Receives tags information from the reader and stores in the database. Using Django Rest Framework.

##### To run the project (Windows PowerShell commands):
1. Make sure you have Python installed
```
…\rfid-tag-django-api> py -V
Python 3.9.6
```
2. Create a python virtual environment
```
…\rfid-tag-django-api> py -m venv env
```
3. Activate the virtual environment
```
…\rfid-tag-django-api> .\env\Scripts\Activate.ps1
```
4. Install the required modules from requirements.txt
```
(env) …\rfid-tag-django-api> pip install -r .\requirements.txt
```
5. Create a file named secrets.py, in the 'tagsProject' directory, for storing the Django Secret Key (and maybe other secrets later)
```
(env) …\rfid-tag-django-api> New-Item -Path .\tagsProject\ -Name "secrets.py" -Value "DJANGO_SECRET_KEY = 'django-insecure-a-random-generated-key'"
```
###### Note: make sure you have 'secrets.py' in the .gitignore file
6. Migrate and run
```
(env) …\rfid-tag-django-api> py .\manage.py makemigrations
(env) …\rfid-tag-django-api> py .\manage.py migrate
(env) …\rfid-tag-django-api> py .\manage.py runserver
```
    
