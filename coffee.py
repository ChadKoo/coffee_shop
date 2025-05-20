from order import Order

class Coffee:
    all = []

    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)

    def orders(self):
        return [order for order in Order.all if order.coffee == self] #all orders for that type of coffee
    
    def customers(self):
        return  list ({order.customer for order in self.orders()}) #Unique list of customers(hence the {}) that have ordered this coffee
    
    def num_orders(self):
        return len([order for order in Order.all if  order.coffee == self]) #total num of orders for that type of coffee
    
    def average_price(self):
        coffee_orders = [order for order in Order.all if  order.coffee == self]#all coffee orders
        if not coffee_orders:
            return 0 #Avoids dvision by 0
        total_price = sum ([order.price for order in coffee_orders]) #sum of all coffee orders
        avg = total_price/len(coffee_orders) #sum of all coffe orders divided by num of those coffee orders
        return avg

    @property
    def name(self):
        return self._name
    
    @name.setter #Coffee validator
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Name of coffee must be a string over 3 characters long")