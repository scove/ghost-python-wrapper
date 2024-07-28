import pytest
from ghost_python_wrapper.ghost_wrapper import GhostWrapper #I don't like this lol

def test_always_passes():
    assert True

def test_creates_object_properly():
    new_ghost = GhostWrapper("http://localhost", "abc-123", "v5.0")
    assert new_ghost.host == "http://localhost"
    assert new_ghost.key == "abc-123"
    assert new_ghost.version == "v5.0"
    