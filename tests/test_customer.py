import pytest
from ..customer import Customer
from coffee import Coffee
from order import Order

def test_customer_initialization():
    customer = Customer("Alice")
    assert customer.name == "Alice"

def test_customer_create_order():
    customer = Customer("Alice")
    coffee = Coffee("Espresso")
    order = customer.create_order(coffee, 5.0)
    assert len(customer.orders()) == 1
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_customer_coffees():
    customer = Customer("Alice")
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Latte")
    customer.create_order(coffee1, 5.0)
    customer.create_order(coffee2, 6.5)
    coffees = customer.coffees()
    assert len(coffees) == 2
    assert coffee1 in coffees
    assert coffee2 in coffees

def test_most_aficionado():
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    coffee = Coffee("Espresso")
    customer1.create_order(coffee, 5.0)
    customer2.create_order(coffee, 6.0)
    aficionado = Customer.most_aficionado(coffee)
    assert aficionado == customer2
