import pytest
from customer import Customer
from coffee import Coffee

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("A")

    coffee = Coffee("Cappuccino")
    assert coffee.name == "Cappuccino"
