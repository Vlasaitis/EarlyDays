import pytest
from project import clues_generator
from project import movie_generator
from project import create_underscores

def test_clues_generator():
    clues_generator("Inception")
    movie = movie_generator("Inception")
    assert movie["Year"] == "2010"

def test_create_underscores():
    movie = create_underscores("Bad Man")
    assert movie == "___ ___"

def test_movie_generator():
    movie = movie_generator("Up")
    assert movie["Title"] == "Up"
    assert movie["Genre"] == "Animation, Adventure, Comedy"