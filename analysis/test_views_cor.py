import pytest
import requests


"""
PyTest to test calculation of correlation for the values in the database
"""

BASE_URL = "http://127.0.0.1:8000/"
USERNAME = 'srisainee'
PASSWORD = 'abc123'
TOKEN = 'cc85f5ac543dce8e97d71aa7cc0deefd6cc1f1af'

#@pytest.mark.django_db
@pytest.mark.parametrize(
   'correlation', [
       ("pearson"),
       ('spearman'),
   ]
)
def test_post(
   correlation
):
   url = BASE_URL + 'analysis/modellessapi/'
   headers = {
       'Authorization': 'Token ' + TOKEN
   }
   kwargs = {
       "headers": headers,
   }
   data = {
       'correlation': correlation,
   }
   response = requests.post(url=url, **kwargs, data=data)
   assert response.status_code == 202

