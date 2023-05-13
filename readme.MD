**Site** for the publication of ads for sale, broken down into rubrics made on Django. Has API created using Django REST API Framework

**How to run:**

1. Clone project by git clone
2. Write next lines in console:
   pip install pipenv
   pipenv install Django
   pipenv shell
   pipenv install django-bootstrap4
   pipenv install easy-thumbnails
   pipenv install django-cleanup
   pipenv install django-simple-captcha
   pip install djangorestframework
   pip install django-cors-headers
3. Make migrations:
   python manage.py makemigrations
   python manage.py migrate
4. Create superuser:
   python manage.py createsuperuser
5. Run server:
   python manage.py runserver
6. Go to /admin and create Superrubrics and Subrrubrics
7. If you want to add image to your advertisement - Paste it in media folder in project core and then select from there

API:
If you want to work with API - send requests to http://localhost:8000/api/bbs/{details}.
Example of request to GET all advertisements:
GET http://localhost:8000/api/bbs/

Example of request to Create new comment:

You can get csrfTokens and session Id from console.

1. Go to console -> Network, on Preserve log
2. Create new comment
3. You will see document 3 in network history. Click on it
4. In request headers you can get session_id and csrftoken. Paste them in headers in sessionid, csrftoken and X-CSRFToken
5. You can get csrfmiddlewaretoken in payload. Paste it in data.
6. You can rewrite curl to any language using https://curlconverter.com/ if you want or look in tests.py in api folder and there you can see example in Python.

curl --location 'http://localhost:8000/api/bbs/3/comments/'
-H 'Cookie: sessionid=uwkbk1hdmfwa5c2ixu5i9mvc5kcybf0g'
-H 'csrftoken: rHIDo2ttXuPZZq23rxrYGm8UuloYrJ3G'
-H 'Cookie: csrftoken=rHIDo2ttXuPZZq23rxrYGm8UuloYrJ3G'
-H 'X-CSRFToken: rHIDo2ttXuPZZq23rxrYGm8UuloYrJ3G'
-H 'Content-Type: application/json'
--data '{

    "csrfmiddlewaretoken": "84CZxS3k7tIcrDAOMwtBEt2sD884bRlSpBasLKmDUNn1gTsH3TKpaF0cXjmSsqeo",

    "bb": 3,

    "author": "admin",

    "content": "api"

}'
