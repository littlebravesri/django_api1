# from django.test import TestCase
import pytest

"""
test PyTest 
"""

@pytest.fixture
def test_correlation():
    print ("abcdefgh")
    assert "abc" == "abc"
