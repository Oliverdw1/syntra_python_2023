import pytest
from fizz_buzz.code.checkout import Checkout, CannotAddItemWithoutPriceError


@pytest.fixture()
def checkout():
    checkout_instance = Checkout()
    return checkout_instance

def test_can_add_item_price(checkout):
    #checkout = Checkout()
    checkout.add_item_price("a",1)


def test_can_calculate_total(checkout):
    #checkout = Checkout()
    assert checkout.calculate_total() == 0
    checkout.add_item_price("a", 10)
    checkout.add_item_price("b", 5)
    checkout.add_item("a")
    checkout.add_item("b")
    assert checkout.calculate_total() == 15

def test_can_add_mult_items_and_get_correct_total(checkout):
    #checkout = Checkout()
    assert checkout.calculate_total() == 0
    checkout.add_item_price("a", 10)
    checkout.add_item_price("b", 5)
    checkout.add_item("a")
    checkout.add_item("a")
    checkout.add_item("a")
    checkout.add_item("b")
    checkout.add_item("b")
    checkout.add_item("b")
    checkout.add_item("b")
    assert checkout.calculate_total() == 50


def test_can_add_discount_rules(checkout):
    #checkout = Checkout()
    checkout.add_discount_rules('a',4,3)


def test_can_apply_discount_rules_to_total(checkout):
    #checkout = Checkout()
    assert checkout.calculate_total() == 0
    checkout.add_item_price("a", 1)
    checkout.add_item_price("b", 2)
    checkout.add_discount_rules('a',4,3)
    checkout.add_discount_rules('b',2,1)

    checkout.add_item("a")
    checkout.add_item("a")
    checkout.add_item("a")
    checkout.add_item("a")
    checkout.add_item("b")
    checkout.add_item("b")
    assert checkout.calculate_total() == 5


def test_raise_exception(checkout):
    with pytest.raises(CannotAddItemWithoutPriceError):
        #checkout = Checkout()
        checkout.add_item_price("a", 1)
        checkout.add_item("a")
        checkout.add_item("b")
