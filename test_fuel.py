import pytest
from fuel import convert, gauge #imports functions from fuel.py

def test_convert():
    # converts fractions into percentages. this is ran throuh the fuel.py to check if all the answers are what they should be.
    assert convert(0.25) == 25
    assert convert(0.75) == 75
    assert convert(0) == 0
    assert convert(1) == 100

def test_gauge():
    # tests if the right vvariable will be printed out depending on the percentages
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(69) == "69%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"


if __name__ == "__main__": 
    
    # runs the tests using pytest
    pytest.main()