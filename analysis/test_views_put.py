import pytest
import requests

"""
PyTest to test update a row in the database
"""

BASE_URL = "http://127.0.0.1:8000/"
USERNAME = 'srisainee'
PASSWORD = 'abc123'
TOKEN = '4798b0ec544485367d2109bdb250e6cce20945f0'


def test_put(
        id = 4, bags_s = 11111, bags_l = 5253.2
    ):
   url = BASE_URL + 'analysis/modelbasedapi/' + str(id) + '/'
   headers = {
       'Authorization': 'Token ' + TOKEN
   }
   kwargs = {
       "headers": headers,
   }
   data = {
        'bags_s' : bags_s,
        'bags_l' : bags_l
   }
   response = requests.put(url=url, **kwargs, data=data)
   assert response.status_code == 201

