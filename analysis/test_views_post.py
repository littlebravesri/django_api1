import pytest
import requests

"""
PyTest to test edit a row in the database
"""

BASE_URL = "http://127.0.0.1:8000/"
USERNAME = 'srisainee'
PASSWORD = 'abc123'
TOKEN = '4798b0ec544485367d2109bdb250e6cce20945f0'


def test_post(
        # date_w=None, price=None, total_vol=None, plu1=None, plu2=None, plu3=None,
        # bags_t=None, bags_s=None, bags_l=None, bags_lx=None, type = None,
        # year=None, location=None
    ):
   url = BASE_URL + 'analysis/modelbasedapi/'
   headers = {
       'Authorization': 'Token ' + TOKEN
   }
   kwargs = {
       "headers": headers,
   }
   data = {
        'date_w' : "24/12/2016",
        'price' : 1.50,
        'total_vol' : 641232.22,
        'plu1' : 999.2,
        'plu2' : 41250.2,
        'plu3' : 88.0,
        'bags_t' : 6666.5,
        'bags_s' : 5574.1,
        'bags_l' : 555.3,
        'bags_lx' : 0.0,
        'type' : "C",
        'year' : 2014,
        'location' : "Albany",
   }
   response = requests.post(url=url, **kwargs, data=data)
   assert response.status_code == 202

