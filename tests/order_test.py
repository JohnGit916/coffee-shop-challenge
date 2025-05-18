import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_validation():
    c = Customer("Tim")
    coffee = Coffee("Flat White")

    with pytest.raises(ValueError):
        Order(c, coffee, 0.5)

    with pytest.raises(ValueError):
        Order(c, coffee, 12.0)

    with pytest.raises(TypeError):
        Order("Tim", coffee, 3.0)

    o = Order(c, coffee, 3.5)
    assert o.price == 3.5
    assert o.customer == c
    assert o.coffee == coffee
