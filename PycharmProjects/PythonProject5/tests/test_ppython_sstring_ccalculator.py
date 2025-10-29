
from src.ppython_sstring_ccalculator import python_add

def test_python_add_empty_string_returns_zero():
    assert python_add("") == 0
def test_single_number_returns_itself():
    assert python_add("1") == 1
    assert python_add("0") == 0
    assert python_add("2") == 2
def test_two_numbers_sum():
    assert python_add("1,3") == 4
    assert python_add("1,2") == 3
    assert python_add("1,1") == 1
    assert python_add("0,1") == 1
    assert python_add("0,2") == 2
    assert python_add("0,3") == 3
    assert python_add("0,10") == 10
    assert python_add("5,15") == 20
    assert python_add("10,30") == 40
    assert python_add("20,40") == 60