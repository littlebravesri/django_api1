[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Django Restful API Example

This project is to help you with the following:
1. To show how to use the Django REST framework
2. As an independent API backend for the example bootstrap project https://github.com/DataDisca/bootstrap1

## Contributors
- Token timeout : [Prabath Hetti Mudiyanselage](https://github.com/prabathbr) \(GitHUB Username: prabathbr\)

## Database Configuration
To use SQLite or PostgreSQL database comment/uncomment the corresponding section of the settings.py 
```python
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
```
Make sure you run migrations after changing the database.

## Using the Rest Framework Interface
You may need to uncomment the following line in the settings.py to use the rest framework interface:
```
# 'rest_framework.authentication.BasicAuthentication',
```
But, it may interfere with the token authentication in the bootstrap theme. Therefore after testing APIs, recomment the above line.

## Token timeout

Configure `settings.py`

 `TOKEN_EXPIRE_TIME = 1500  # Seconds,`

## New features in this version
- Token timeout
  

## Sponsor
DataDisca Pty Ltd, Melbourne, Australia

[https://www.datadisca.com](https://www.datadisca.com)


