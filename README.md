[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Django Restful API Example

This project is to help you with the following:
1. To show how to use the Django REST framework
2. As an independent API backend for the example bootstrap project https://github.com/DataDisca/bootstrap1

## Contributors
- Token timeout : [Prabath Hetti Mudiyanselage](https://github.com/prabathbr) \(GitHub Username: prabathbr\)

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

## Starting Django Automatically 
In production environments, Django should automatically start When the machine starts or reboots.
Follow the steps given below. 
1. Modify the script [start_django.sh](./start_django.sh) for your environment.
    1. Configure the path of your Django installation  
        ``` cd <your path> ```
    1. Change the following to suit your Django installation  
        ``` Change 0.0.0.0:8000 to suit your listening IP and port ```  
        ```Change django.log to your preferred logfile location. Using this default is a bad idea as it would fill up your Django folder```

1. Create a cron entry:
```
*/5 * * * * /usr/bin/sh /d/data/dd_projects/django_api/start_django.sh &
 ``` 
The cron job will run every 5 minutes. It will check if the Django is running. 
If not it will start Django. 
You can change the interval to different value for your requirement.

## New features in this version
- Starting Django automatically
  

## Sponsor
DataDisca Pty Ltd, Melbourne, Australia

[https://www.datadisca.com](https://www.datadisca.com)


