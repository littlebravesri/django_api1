import pytest
import requests

"""
PyTest to check if username, current password match the observations in the database and 
perform appropriate operations 
"""

BASE_URL = "http://127.0.0.1:8000/"
USERNAME = 'srisainee'
PASSWORD = 'abc123'
TOKEN = 'da6aa1327b15f1f891acd086dd66762466de51e6'


#@pytest.mark.django_db
@pytest.mark.parametrize(
   'username, cur_password, new_password, status_code', [
       ('srisainee', 'something', 'something', 400),
       ('something', 'something', 'something', 404),
        ('srisainee', 'newpassword', 'chnagepassword', 200),
   ]
)
def test_post(
   username, cur_password, new_password, status_code
):
   url = BASE_URL + 'app_user/'
   headers = {
       'Authorization': 'Token ' + TOKEN
   }
   kwargs = {
       "headers": headers,
   }
   data = {
       'username': username,
        'currentPassword': cur_password,
        'newPassword': new_password,
   }
   response = requests.post(url=url, **kwargs, data=data)
   assert response.status_code == status_code

