from customer import Customer
from coffee import Coffee
from order import Order

# Create some customer instances
customer1 = Customer("Alice")
customer2 = Customer("Bob")

# Create some coffee instances
coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")

# Create some orders
order1 = customer1.create_order(coffee1, 5.0)  # Alice orders Espresso
order2 = customer1.create_order(coffee2, 6.5)  # Alice orders Latte
order3 = customer2.create_order(coffee1, 4.5)  # Bob orders Espresso

# View customer orders
print(f"{customer1.name} ordered: {[coffee.name for coffee in customer1.coffees()]}")
print(f"{customer2.name} ordered: {[coffee.name for coffee in customer2.coffees()]}")

# View coffee orders
print(f"Total orders for {coffee1.name}: {coffee1.num_orders()}")
print(f"Average price for {coffee1.name}: {coffee1.average_price()}")

# Check the most aficionado (bonus task)
aficionado = Customer.most_aficionado(coffee1)
if aficionado:
    print(f"The customer who spent the most on {coffee1.name} is {aficionado.name}.")
else:
    print(f"No orders for {coffee1.name}.")
