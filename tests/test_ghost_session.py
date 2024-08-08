import pytest
from unittest.mock import patch, Mock, call
from ghost_python_wrapper.ghost_session import GhostSession #I don't like this lol


@patch('ghost_python_wrapper.ghost_session.GhostSession.basic_auth')
def test_ghost_wrapper_creates_properly(mock_auth):
    new_ghost = GhostSession("http://localhost", "v5.0", "jimmy", "qwerty123")
    assert new_ghost.host == "http://localhost"
    assert new_ghost.version == "v5.0"
    assert new_ghost.username == "jimmy"
    assert new_ghost.password == "qwerty123"

@patch('ghost_python_wrapper.ghost_session.GhostSession.basic_auth')
def test_ghost_wrapper_calls_basic_auth(mock_auth):
    GhostSession("http://localhost", "v5.0", "jimmy", "qwerty123") #maybe make a fixture here
    assert mock_auth.called

@patch('requests.utils.dict_from_cookiejar')
@patch('requests.post')
def test_basic_auth_should_call_post_properly(mock_post, mock_jar):
    mock_object = Mock(host='localhost', username='jimmy', password="qwerty123")
    mock_post.return_value = Mock(status_code=201)
    GhostSession.basic_auth(mock_object)
    assert mock_post.call_args == call('localhost', data={'username': 'jimmy', 'password': 'qwerty123'})

@patch('requests.utils.dict_from_cookiejar')
@patch('requests.post')
def test_basic_auth_should_raise_exception_when_status_code_not_201(mock_post, mock_jar):
    mock_object = Mock(host='localhost', username='????', password="qwerty123")
    mock_post.return_value = Mock(status_code=404)
    with pytest.raises(Exception):
        GhostSession.basic_auth(mock_object)

@patch('requests.utils.dict_from_cookiejar')
@patch('requests.post')
def test_basic_auth_should_call_dict_from_cookiejar_properly(mock_post, mock_jar):
    mock_object = Mock(host='localhost', username='jimmy', password="qwerty123")
    mock_post.return_value = Mock(status_code=201, cookies={1: "I am a cookie, hello"})
    GhostSession.basic_auth(mock_object)
    assert mock_jar.call_args == call({1: "I am a cookie, hello"})

@patch('requests.utils.dict_from_cookiejar')
@patch('requests.post')
def test_basic_auth_should_return_proper_cookie(mock_post, mock_jar):
    mock_object = Mock(host='localhost', username='jimmy', password="qwerty123")
    mock_post.return_value = Mock(status_code=201, cookies={'ghost-admin-api-session': "I am a cookie, hello"})
    mock_jar.return_value = {'ghost-admin-api-session': "I am a cookie, hello"}
    assert GhostSession.basic_auth(mock_object) == {'ghost-admin-api-session': "I am a cookie, hello"}