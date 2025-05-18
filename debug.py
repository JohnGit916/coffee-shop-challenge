from customer import Customer
from coffee import Coffee
from order import Order

# Sample usage
c1 = Customer("Alice")
c2 = Customer("Bob")

coffee1 = Coffee("Latte")
coffee2 = Coffee("Mocha")

c1.create_order(coffee1, 4.5)
c1.create_order(coffee2, 5.5)
c2.create_order(coffee1, 4.0)

print("Coffees ordered by Alice:", [c.name for c in c1.coffees()])
print("Orders for Latte:", coffee1.num_orders())
print("Average price for Latte:", coffee1.average_price())
print("Top spender on Latte:", Customer.most_aficionado(coffee1).name)
