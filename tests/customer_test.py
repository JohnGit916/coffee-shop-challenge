import pytest
from customer import Customer
from coffee import Coffee

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("")

    with pytest.raises(ValueError):
        Customer("A" * 16)

    c = Customer("John")
    assert c.name == "John"

def test_customer_create_order_and_relationships():
    c = Customer("Anna")
    coffee = Coffee("Espresso")
    c.create_order(coffee, 3.0)

    assert coffee in c.coffees()
    assert len(c.orders()) == 1
def test_customer_most_aficionado_returns_customer_with_highest_spending():
    cust1 = Customer("Alex")
    cust2 = Customer("Jamie")
    coffee = Coffee("Cappuccino")

    cust1.create_order(coffee, 4.0)
    cust1.create_order(coffee, 2.0)
    cust2.create_order(coffee, 3.0)

    assert Customer.most_aficionado(coffee) == cust1
