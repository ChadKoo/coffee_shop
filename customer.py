from order import Order

class Customer:
    all = []
    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    def orders(self):
        return [order for order in Order.all if order.customer == self] #all orders for this customer
    
    def coffees(self):
        return list ({order.coffee for order in self.orders()}) #unique list of coffees this customer has ordered
    
    def create_order(self, coffee, price):
        return Order(customer = self, coffee = coffee, price = price) #creates a new order for this customer with given coffee and price
    
    @classmethod
    def most_aficionado(self, coffee):
        customer_spending = {} #tracks how much each customer spends on a particular coffee

        for order in Order.all: #Loop through all orders
            if order.coffee == coffee :#Add price of the coffee if coffee matches
                if order.coffee in customer_spending:
                    customer_spending[order.customer] += order.price
                else:
                    customer_spending[order.customer] = order.price #Add price of coffee

        if not customer_spending: #Return none if no customers ordered that coffee
            return None
    
        return max(customer_spending, key=customer_spending.get) #return customer that spent most

    @property
    def name(self):
        return self._name 
    
    @name.setter#Customer name validator
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <=15:
            self._name = name
        else:
            raise ValueError("Customer name must be a string between 1 and 15 characters")
        