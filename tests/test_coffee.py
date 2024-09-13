import pytest
from ..coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_initialization():
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"

def test_coffee_orders():
    coffee = Coffee("Espresso")
    customer = Customer("Alice")
    customer.create_order(coffee, 5.0)
    orders = coffee.orders()
    assert len(orders) == 1
    assert orders[0].coffee == coffee

def test_coffee_customers():
    coffee = Coffee("Espresso")
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    customer1.create_order(coffee, 5.0)
    customer2.create_order(coffee, 6.0)
    customers = coffee.customers()
    assert len(customers) == 2
    assert customer1 in customers
    assert customer2 in customers

def test_coffee_num_orders():
    coffee = Coffee("Espresso")
    customer = Customer("Alice")
    customer.create_order(coffee, 5.0)
    customer.create_order(coffee, 6.0)
    assert coffee.num_orders() == 2

def test_coffee_average_price():
    coffee = Coffee("Espresso")
    customer = Customer("Alice")
    customer.create_order(coffee, 5.0)
    customer.create_order(coffee, 6.0)
    assert coffee.average_price() == 5.5
