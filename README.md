# django_api1
Django Restful API Example

This project is to help you with the following:
1. To show how to use the Django REST framework
2. As the independant API backend for the example bootstrap project https://github.com/mbtl-datadisca/bootstrap1

Using SQLite or PostgreSQL database comment/uncomment the corresponding section of the settings.py 

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dj_api',
        'USER': 'xxx',
        'PASSWORD': 'xxxxx',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Make sure you run migrations after changing the database.

You may need to uncomment the following line of the settings.py to use the rest framework interface:
# 'rest_framework.authentication.BasicAuthentication',
But it may infere with the Token authentication with the bootstrap theme. Therefore after testing APIs, please recomment the above line.

You can expand this with more APIs.


