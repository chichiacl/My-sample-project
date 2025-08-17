from bank import value
import pytest

def test_zero():
    assert value("Hello") == 0
    assert value("HeLlo, w0rld") == 0
    assert value("Hello!") == 0
    assert value("How you doing?") == 20
    assert value("What's happening?") == 100


def test_incorrect_values():
    ...

def test_case_sensitive():
    ...


def test_entire_phrase():
    ...
