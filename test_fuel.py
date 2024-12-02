import pytest
from fuel import convert, gauge

def test_convert():
    assert convert(0.25) == 25
    assert convert(0.75) == 75
    assert convert(0) == 0
    assert convert(1) == 100

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(69) == "69%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"


if __name__ == "__main__":
    pytest.main()