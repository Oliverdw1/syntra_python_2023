import pytest
from unit_testsw.leap_year import Leapyear


def test_divisbible_by_400():
    leapyear = Leapyear(400)
    assert leapyear.is_leap_year() == True


def test_divisible_by_100_and_not_400():
    leapyear = Leapyear(100)
    assert leapyear.is_leap_year() == False


def test_divisible_by_4_but_not_100():
    leapyear = Leapyear(2008)
    assert leapyear.is_leap_year() == True


def test_not_divisible_by_4():
    leapyear = Leapyear(2013)
    assert leapyear.is_leap_year() == False


