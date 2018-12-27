#import pytest

from SimpleNumber import issimple

def test_SimpleNumber_trivial():
    assert issimple(3) == True

def test_SimpleNUmber_positiv():
    assert issimple(1163) == True

def test_SimpleNumber_negativ():
    assert issimple(3027) == False

