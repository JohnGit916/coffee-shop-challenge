from order import Order

class Customer:
    _all = []

    def __init__(self, name):
        self.name = name
        Customer._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        return [order for order in Order._all if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        spending = {}
        for order in coffee.orders():
            spending[order.customer] = spending.get(order.customer, 0) + order.price
        return max(spending, key=spending.get) if spending else None
    @classmethod
    def most_aficionado(cls, coffee):
        highest_spender = None
        max_spent = 0
        for customer in cls._all:
            total_spent = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total_spent > max_spent:
                max_spent = total_spent
                highest_spender = customer
        return highest_spender if max_spent > 0 else None
