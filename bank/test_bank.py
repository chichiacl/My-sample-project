from bank import value
import pytest

def test_zero():
    assert value("Hello") == 0
    assert value("HeLlo, w0rld") == 0
    assert value("Hello!") == 0

def test_twenty():
    assert value("How you doing?") == 20
    assert value("H  ") == 20
    assert value("Hello.") == 20

def test_hundred():
    assert value("What's happening?") == 100
    assert value("Welcome to the bank.") == 100
    assert value("123! client 123!") == 100

def test_error():
    with pytest.raises(TypeError):
        value(100)







