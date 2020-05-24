"""
Purpose: Data types used in DataDisca applications are defined here

Developers:
<Your Name(s)>

Sponsor: DataDisca Pty Ltd. Australia
https://github.com/DataDisca
"""
import json
import pytest
import requests

BASE_URL = "http://127.0.0.1:8000/"
USERNAME = 'tlk'
PASSWORD = 'tlk12345'


@pytest.fixture(scope="class", name="auth_paras")
def get_auth_paras():
    class AuthParas:
        def __init__(self):
            self.token = None
    return AuthParas()


class TestAuth:

    def test_login(self, auth_paras):
        url = BASE_URL + 'login'
        data = {
            'username': USERNAME,
            'password': PASSWORD
        }
        kwargs = {
            "data": data
        }
        response = requests.post(url=url, **kwargs)
        if response.status_code == 200:
            _dict = json.loads(response.text)
            if 'token' in _dict.keys():
                auth_paras.token = _dict['token']
                if len(auth_paras.token) > 0:
                    assert True
                    return

        assert False

    def test_items(self, auth_paras):
        url = BASE_URL + 'items/'
        headers = {
            'Authorization': 'Token ' + auth_paras.token
        }
        kwargs = {
            "headers": headers
        }
        response = requests.get(url=url, **kwargs)
        _dict = json.loads(response.text)
        if 'count' in _dict.keys():
            if _dict['count'] > 0:
                assert True
                return

        assert False

