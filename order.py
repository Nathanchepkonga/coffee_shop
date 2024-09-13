class Order:
    orders = []

    def __init__(self, customer, coffee, price):
        from customer import Customer  # Import locally to avoid circular import
        from coffee import Coffee
        
        if not isinstance(customer, Customer):
            raise ValueError("Invalid customer")
        if not isinstance(coffee, Coffee):
            raise ValueError("Invalid coffee")
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.orders.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price
