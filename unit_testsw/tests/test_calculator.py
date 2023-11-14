import pytest
from unit_testsw.calculator import Calculator

def test_print_string():
    calculator = Calculator()
    assert calculator.print_string(string="hello") == "hello"


def test_add():
    calculator = Calculator()
    assert calculator.add("1,2") == 3
    assert calculator.add("1") == 1
    assert calculator.add("1,4,4") == 9
    assert calculator.add("1,4,4,6,10") == 25



def test_add2():
    calculator = Calculator()
    assert calculator.add("1\n2") == 3
    assert calculator.add("1") == 1
    assert calculator.add("1\n4\n4") == 9
    assert calculator.add("1\n4\n4\n6\n10") == 25
    assert calculator.add("0") == 0
    assert calculator.add("") == 0
    assert calculator.add("1,4\n4,6\n10") == 25



