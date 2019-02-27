import pytest
from classes import Die

favoriteDie = Die(6)

def test_cast_me():
    favoriteDie.cast_me()