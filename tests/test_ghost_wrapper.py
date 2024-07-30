import pytest
from unittest.mock import patch
from ghost_python_wrapper.ghost_wrapper import GhostWrapper #I don't like this lol

def test_always_passes():
    assert True

def test_ghost_wrapper_creates_properly():
    new_ghost = GhostWrapper("http://localhost", "v5.0", "jimmy", "qwerty123")
    assert new_ghost.host == "http://localhost"
    assert new_ghost.version == "v5.0"
    assert new_ghost.username == "jimmy"
    assert new_ghost.password == "qwerty123"

@patch('ghost_python_wrapper.ghost_wrapper.GhostWrapper.basic_auth')
def test_ghost_wrapper_calls_basic_auth(mock_auth):
    GhostWrapper("http://localhost", "v5.0", "jimmy", "qwerty123") #maybe make a fixture here
    assert mock_auth.called
    