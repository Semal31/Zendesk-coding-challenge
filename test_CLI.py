import pytest
from helper import getInput

# wanted to put all helper tests in their own class but setattr would not work in the class
def test_getInput_charArray_correct(monkeypatch):
  monkeypatch.setattr('builtins.input', lambda: "a")
  assert getInput("example prompt", ['a', 'b']) == 'a'

def test_getInput_char_correct(monkeypatch):
  monkeypatch.setattr('builtins.input', lambda: "a")
  assert getInput("example prompt", 'a') == 'a'

def test_getInput_char_incorrect(monkeypatch):
  monkeypatch.setattr('builtins.input', lambda: "a")
  assert getInput("example prompt", 'a') != 'b'

def test_getInput_charArray_incorrect(monkeypatch):
  monkeypatch.setattr('builtins.input', lambda: "a")
  assert getInput("example prompt", ['a', 'b']) != 'c'