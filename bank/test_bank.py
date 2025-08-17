from bank import value
import pytest

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO there") == 0
    assert value("hello!") == 0
    assert value("hello, world") == 0

def test_h():
    assert value("hi") == 20
    assert value("hey there") == 20
    assert value("howdy") == 20
    assert value("Hmmm") == 20

def test_not_h():
    assert value("What's up") == 100
    assert value("Good morning") == 100
    assert value("Bye") == 100
    assert value("Ahoy") == 100
