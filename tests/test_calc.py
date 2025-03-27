import pytest

def add(a,b):
    return a + b

def test_add():
    assert add(2,3) == 5

# def test_add():
#     assert add(2,3) == 55

@pytest.mark.parametrize("a,b,wynik",[
    (2,3,5),
    (3,5,12),
    (22,33,12)
])

def test_param_add(a,b,wynik):
    assert add(a,b) == wynik
