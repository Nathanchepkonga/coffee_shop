import pytest
from ..order import Order
from ..customer import Customer
from ..coffee import Coffee


def test_order_initialization():
    customer = Customer("Alice")
    coffee = Coffee("Espresso")
    order = Order(customer, coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_order_invalid_customer():
    coffee = Coffee("Espresso")
    with pytest.raises(ValueError):
        Order("InvalidCustomer", coffee, 5.0)

def test_order_invalid_coffee():
    customer = Customer("Alice")
    with pytest.raises(ValueError):
        Order(customer, "InvalidCoffee", 5.0)

def test_order_invalid_price():
    customer = Customer("Alice")
    coffee = Coffee("Espresso")
    with pytest.raises(ValueError):
        Order(customer, coffee, 15.0)
