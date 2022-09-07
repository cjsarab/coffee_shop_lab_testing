class Customer:
    
    def __init__(self, name, wallet, age, energy_level):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.energy_level = energy_level

    def buy_a_drink(self, coffee_shop, drink):
        if self.age > 15 and self.energy_level < 110:
        # reducing the money in its wallet 
            self.wallet -= drink.price
        #  increasing the money in the Coffee Shop's till
            coffee_shop.till += drink.price
        #   increasing energy level by caffeine level
            self.energy_level += drink.caffeine_level

