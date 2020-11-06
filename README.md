# quatro-backend-dev-test

Quatro dev backend test.
The goal of this test is to assess your familiarity with building REST APIs and concepts related to building REST APIs with Django. You'll be building an API that enables any developer with an API Key to query the list of restaurants in a 3km radius given a set of GPS coordinates.

---

## Running the project

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv env
```

That will create a new folder `env` in your project directory. Next activate it with this command on mac/linux:

```
source env/bin/active or venv\Scripts\activate.bat(windows)
```

Then install the project dependencies with

```
pip install -r requirements.txt
```

After you need to do migrations and create a superuser

```
 * python manage.py makemigrations
 * python manage.py migrate
 * python manage.py createsuperuser
```

To finish you will need Geodjango. Please folow these link

```
https://docs.djangoproject.com/en/3.1/ref/contrib/gis/install/
```

Now you can run the project with this command

```
python manage.py runserver
```

Details

```
This is an project with an app api using to build an API with the Django Rest Framework. The endpoints of this API are:

# `/register/`: This endpoint receives `{name, username, password}` and creates an account from the information given.
# `/login/`: This endpoint receives `{username, password}` and responds with an access token that a client can use to authenticate themselves for subsequent calls.
# `/api_keys/` [login required]: A `GET` endpoint that responds with the current user's API Keys. Note that these keys (public and secret) are generated when a user creates an account.
# `/restaurants/` [API key pair required]: A `POST` endpoint that given `{lat, lng}` returns the list of restaurants in a 3km radius of those coordinates. Note that this endpoint is only accessible with a valid API key pair specified in the header with `X-Public-Key` and `X-Secret-Key` for the public and secret key respectively.
```