from customer import Customer
from coffee import Coffee

class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer #returns customer instance
        self.coffee = coffee #returns coffee instance
        self.price = price
        Order.all.append(self)

    @property
    def customer(self):
        return self.customer
    
    @customer.setter #Customer validator
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be an instance of customer class")
        self._customer = customer

    @property 
    def coffee(self):
        return self._coffee
    
    @coffee.setter #Coffee validator
    def coffee(self, coffee):
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be an instance of coffee class")
        self._coffee = coffee

    @property
    def price(self):
        return self._price
    
    @price.setter #price validator
    def price(self, price):
        if isinstance(price, float) and 1.0 <= price <= 10.0:
            self._price =  price
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0")
