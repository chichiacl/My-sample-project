from plates import is_valid
import pytest

def test_non_alnum():
    assert is_valid("WE_GUD") == False
    assert is_valid("CS.50") == False
    assert is_valid("HELO 1") == False
    assert is_valid("HELLO1") == True

def test_begining_two_lettes():
    assert is_valid("CS50") == True
    assert is_valid("F1RACE") == False
    assert is_valid("2AMAN") == False
    assert is_valid("1234") == False

def test_for_first_zero():
    assert is_valid("CS05") == False
    assert is_valid("CS500") == True
    assert is_valid("AA0111") == False
    assert is_valid("CS000") == False

def test_for_number_inbetween():
    assert is_valid("H3LL0") == False
    assert is_valid("CC400") == True
    assert is_valid("WE404L") == False
    assert is_valid("HMM123") == True

def test_length():
    assert is_valid("CS50") == True
    assert is_valid("C") == False
    assert is_valid("HELLOCS50") == False
    assert is_valid("AA") == True
    assert is_valid("HELLOC") == True




