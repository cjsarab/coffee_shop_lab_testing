import unittest
from src.customer import Customer
from src.coffee_shop import CoffeeShop
from src.drink import Drink
from src.food import Food

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("John Smith", 50.00, 28, 100)
        # self.drink1 = Drink("Latte", 2.50, 5)
        # self.drink2 = Drink("Mocha", 3.50, 10)
        # self.food = Food("Burger", 8.00, 50)

        self.stock = [
                    {   "type": "drink",
                        "name" : "Latte",
                        "price": 2.50,
                        "energy": 5
                        },
                    {   "type": "drink",
                        "name" : "Mocha",
                        "price": 3.50,
                        "energy": 10
                        },
                    {   "type": "food",
                        "name" : "Burger",
                        "price": 8.00,
                        "energy": 50
                        }
                ]
        self.coffee_shop = CoffeeShop("the Prancing Pony", 200.00, self.stock)

    def test_buy_a_drink(self):
        
        self.customer.buy_a_drink(self.coffee_shop, self.stock[0])
        self.assertEqual(self.customer.wallet, 47.50)
        self.assertEqual(self.coffee_shop.till, 202.50)

    def test_age(self):

        self.customer = Customer("Underage Child", 6.70, 13, 200)
        self.customer.buy_a_drink(self.coffee_shop, self.stock[0])
        self.assertEqual(self.customer.wallet, 6.70)
        self.assertEqual(self.coffee_shop.till, 200.00)

    def test_energy_increased_by_caffeine_level(self):
        self.customer.buy_a_drink(self.coffee_shop, self.stock[0])
        self.assertEqual(105, self.customer.energy_level)

    def test_refuse_sale_high_energy(self):
        self.customer.buy_a_drink(self.coffee_shop, self.stock[1])
        self.customer.buy_a_drink(self.coffee_shop, self.stock[1])
        self.assertEqual(110, self.customer.energy_level)

    def test_rejuvenation_level_change(self):
        self.customer.buy_food(self.coffee_shop, self.stock[2])
        self.assertEqual(50, self.customer.energy_level)
