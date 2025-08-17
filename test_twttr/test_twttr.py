import pytest
from twttr import shorten

def test_shorten():
    assert shorten("Twitter") == "Twitter"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert()

