from bank import value
import pytest

def test_hello():
    assert value("HELLO") == 0
    assert value("hello") == 0
    assert value("Hello, world") == 0
    assert value("Hello!") == 0

def test_h():
    assert value("Heyy.") == 20
    assert value("HEY!") == 20
    assert value("hEY, you.") == 20
    assert value("hey") == 20

def test_not_h():
    assert value("Welcome, you") == 100
    assert value("123") == 100
    assert value("GOOD DAY!") == 100
    assert value("Aye") == 100
