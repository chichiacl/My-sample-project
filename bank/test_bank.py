from bank import value
import pytest

def test_hello():
    assert value("Hello") == 0
    assert value("Hello, world") == 0
    assert value("Hello!") == 0

def test_h():
    assert value("How you doing?") == 20
    assert value("How can i help you") == 20
    assert value("Hello.") == 20

def test_rest():
    assert value("What's happening?") == 100
    assert value("Welcome to the bank.") == 100
    assert value("123! client 123!") == 100


