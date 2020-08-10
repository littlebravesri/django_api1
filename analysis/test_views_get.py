import pytest
import requests

"""
PyTest to test display a row in the database
"""

BASE_URL = "http://127.0.0.1:8000/"
USERNAME = 'srisainee'
PASSWORD = 'abc123'
TOKEN = 'da6aa1327b15f1f891acd086dd66762466de51e6'

#@pytest.mark.django_db
@pytest.mark.parametrize(
   'id', [
       (4),
        (41393162340),
   ]
)
def test_get(
   id
):
   url = BASE_URL + 'analysis/modelbasedapi/' + str(id) + '/'
   headers = {
       'Authorization': 'Token ' + TOKEN
   }
   kwargs = {
       "headers": headers,
   }
   response = requests.get(url=url, **kwargs)
   assert response.status_code == 200

