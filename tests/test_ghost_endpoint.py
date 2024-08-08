import pytest
from unittest.mock import patch, Mock, call
from ghost_python_wrapper.endpoint import Endpoint


def test_should_create_endpoint_properly():
    e = Endpoint('http://localhost:2368/ghost/api/admin/', 'posts/')
    assert e.end_point == 'posts/'
    assert e.full_path == 'http://localhost:2368/ghost/api/admin/posts/'

def test_should_be_able_to_get_content():
    e = Endpoint('http://localhost:2368/ghost/api/admin/', 'posts/')
    content = e.get()

    assert False