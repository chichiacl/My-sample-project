import pytest
from twttr.py import shorten

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"

test_shorten()
