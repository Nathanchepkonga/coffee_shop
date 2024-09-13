class Customer:
    def __init__(self, name):
        from order import Order  # Import locally to avoid circular import

        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Name must be a string between 1 and 15 characters")

    @property
    def name(self):
        return self._name

    def orders(self):
        from order import Order  # Import locally to avoid circular import
        return [order for order in Order.orders if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        from order import Order  # Import locally to avoid circular import
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order  # Import locally to avoid circular import
        
        customers_spending = {}
        for order in coffee.orders():
            if order.customer in customers_spending:
                customers_spending[order.customer] += order.price
            else:
                customers_spending[order.customer] = order.price

        if customers_spending:
            return max(customers_spending, key=customers_spending.get)
        return None
