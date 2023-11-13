import pytest
from test_driven.app.code import (add, reverse_string, max_number, is_even, filter_even_numbers, concatenate_strings,
                                  is_prime, factorial2, reverse_list)


def test_add():
    assert add(1, 2) == 3
    assert add(10, 15) == 25


def test_reverse_string():
    assert reverse_string("hallo") == "ollah"
    assert reverse_string("hello world") == "dlrow olleh"


def test_max_number():
    assert max_number(1, 2) == 2
    assert max_number(10, 5) == 10


def test_is_even():
    assert is_even(4) is True
    assert is_even(3) is False
    assert is_even(2) is True
    assert is_even(13345732836442242421) is False


def test_filter_even_numbers():
    assert filter_even_numbers([2, 5, 6, 1, 8, 9]) == [2, 6, 8]


def test_concatenate_string():
    assert concatenate_strings("hello", "world") == "helloworld"


def test_is_prime():
    assert is_prime(3) is True
    assert is_prime(5) is True
    assert is_prime(4) is False


def test_factorial2():
    assert factorial2(10) == 3628800


def test_reverse_list():
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert reverse_list([1]) == [1]
    assert reverse_list([1, 1, 3, 1, 1]) == [1, 1, 3, 1, 1]
