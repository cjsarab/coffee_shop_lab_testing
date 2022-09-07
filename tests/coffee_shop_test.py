import unittest
from src.coffee_shop import CoffeeShop

class TestCoffeeShop(unittest.TestCase):
    
    def setUp(self):
        self.coffee_shop = CoffeeShop("The Prancing Pony", 100.00,["latte", "mocha"])

    def test_coffee_shop_has_name(self):
        self.assertEqual("The Prancing Pony", self.coffee_shop.name)

    def test_increase_till(self):
        self.coffee_shop.increase_till(2.50)
        self.assertEqual(102.50 , self.coffee_shop.till)

    