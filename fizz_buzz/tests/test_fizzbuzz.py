import pytest
from fizz_buzz.code.fizzbuzz import fizzbuzz


def test_can_call_fizzbuzz():
    fizzbuzz(0)


def test_fizz_buzz_with_0():
    assert fizzbuzz(0) == "fizzbuzz"


def test_fizzbuzz_with_1():
    assert fizzbuzz(1) == 1

def test_fizzbuzz_with_3():
    assert fizzbuzz(3) == "fizz"

def test_fizzbuzz_with_5():
    assert fizzbuzz(5) == "buzz"

def test_fizzbuzz_with_6():
    assert fizzbuzz(6) == "fizz"

def test_fizzbuzz_with_10():
    assert fizzbuzz(10) == "buzz"

def test_fizzbuzz_with_15():
    assert fizzbuzz(15) == "fizzbuzz"

def test_fizzbuzz_with_30():
    assert fizzbuzz(30) == "fizzbuzz"