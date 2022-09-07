class Customer:
    
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age

    def buy_a_drink(self, coffee_shop, drink):
        # reducing the money in its wallet 
        self.wallet -= drink.price
        #  increasing the money in the Coffee Shop's till
        coffee_shop.till += drink.price

