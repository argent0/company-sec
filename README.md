## TODO

* Edit an evaluation
* List evaluations
* Filter evaluation list
* Reports. I'd like to see the data first
* Add date to the evaluation result

## Heroku

* check the logs

```
heroku logs --tail
```

* Host the project with `gunicorn`
`gunicorn` is how heroku hosts the project

```
gunicorn company_sec.wsgi
```

* Freeze the requirements

```
pip install dj-database-url
pip install gunicorn
pip freeze > requirements.txt
```

* Create runtime.txt file

```
$ cat runtime.txt
python-3.7.3
```

* Create the app in heroku

```
$ heroku create
https://sheltered-peak-28439.herokuapp.com/ | https://git.heroku.com/sheltered-peak-28439.git
```

* Configure django for production (incomplete)

``` settings.py
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
DEBUG=False

# at the end
import dj_database_url
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
```

Use
```
export DATABASE_URL="postgres://localhost:5432/company-sec"
```
to run in develpment


* Deploy

app.json
```
Write something in app.json
```

Procfile

```
$ cat Procfile
web: gunicorn gettingstarted.wsgi --log-file -
```

```
git commit
git push heroku master
```
take note of the name: 

* Make sure that one instance is running
```
heroku ps:scale web=1
```

* Migrate the database
```
heroku run python company_sec/manage.py migrate
```

* Check logs

```
$ heroku logs --tail
```

* Postgress

+ Check configuration

```
heroku config
heroku pg
```

+ shell

```
heroku pg:psql
```

* Static files

Django doesn't serve static files in production. By design.

```
pip install whitenoise
# remember to freeze
```

settings.py
```
MIDDLEWARE = [
	# After django securyty
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

## Step by Step

* Create a python environment
* Install django, djangorestframework, pyscopg2
* Create Django project
* Create Django app
* Delete the postgress database if it already exists
* Create the postgress database
* Configure postgress as the django database backend
* Migrate the database
* Run the django server to check that it's working so far
* Create the application inside the project directory. You should have

```
$ pwd
<some path>/tutorial
(python-environment) $ find . -type f -name '*.py'
./manage.py
./vbsite/wsgi.py
./vbsite/asgi.py
./vbsite/__init__.py
./vbsite/settings.py
./vbsite/urls.py
./api/tests.py
./api/apps.py
./api/admin.py
./api/__init__.py
./api/models.py
./api/serializers.py
./api/urls.py
./api/views.py
```
* Add the app to the installed apps in settings.py
* Migrate `python manage.py migrate`
* Add the users
* Create some models in the app

## Credentials

**User**: admin **Pass**: non-pass
**User**: david **Pass**: non-pass

## Examples

Create a tag using the API

```
http --auth david:non-pass --form POST http://127.0.0.1:8000/api/tags/create/ number=123
```

## Django

**Install**

```
pip install django
```

**Run the server**

```
python mange.py runserver
```

**Create a project**

```
django-admin startproject mysite
```

**Create an app**

```
django-admin startapp myapp
```

**Populate the database**

```
python manage.py migrate
```

*After changes in the models*

Generate a migration

```
python manage.py makemigrations myapp
```

**Create admin user**

```
python manage.py createsuperuser
```

**Using users**

urls.py
```
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
]
```

## Django rest framework

**Install**

```
pip install djangorestframework
```

**Generate the api scheme**
```
python manage.py generateschema > api.scheme
```

### Tutorial

https://www.django-rest-framework.org/tutorial/1-serialization/

## Django CORS headers

To allow requests from diffetent domains

see: https://github.com/adamchainz/django-cors-headers

## Virtial environment

**Create**
```
python3 -m venv tutorial-env
```

**Activate**

```
source tutorial-env/bin/activate
```

**Install**

```
pip install super-duper-lib
```

**Create requirements.txt**

```
pip freeze > requirements.txt
```

**Install from requirements**

```
pip install -r requirements.txt
```

## Postgress

**Install python lib**

```
pip install psycopg2
```
**Create DataBase**

```
createdb data_base_name
```

**Drop or Delete DataBase**
```
dropdb data_base_name
```

**Set postgresql in django**

```
'default': {
	'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'vb',
}
```

## JSON Web Tocken (JWT)

https://github.com/davesque/django-rest-framework-simplejwt

Authentication method for web apps.

```
pip install djangorestframework_simplejwt
```

at settings.py
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
```

at urls.py
```
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # Your URLs...
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
```

Obtain Token

```
http post http://127.0.0.1:8000/api/token/ username=vitor password=123
```

Access API
```
http GET http://127.0.0.1:8000/your-api/ "Authorization: Bearer <access token>"
```

Refresh token
```
http post http://127.0.0.1:8000/api/token/refresh/ refresh=<refresh token>"
```

## Angular

Initial setup

```
npm install -g @angular/cli

ng new my-web-app
cd my-web-app
ng serve
```

**Angular JWT**

Create the auth service

```
ng generate service auth
```

**Create a component**

```
ng generate component hero
```

**Create a service**
```
ng generate service auth
```

## Bootstrap (fot the angular app)

https://ng-bootstrap.github.io/#/getting-started

In the web-app folder
```
npm install --save bootstrap
npm install --save @ng-bootstrap/ng-bootstrap
```


