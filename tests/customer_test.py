import unittest
from src.customer import Customer
from src.coffee_shop import CoffeeShop
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("John Smith", 50.00, 28)
        self.drink1 = Drink("Latte", 2.50)
        self.drink2 = Drink("Mocha", 3.50)

        drinks = [self.drink1, self.drink2]
        self.coffee_shop = CoffeeShop("the Prancing Pony", 200.00, drinks)

    def test_buy_a_drink(self):
        
        self.customer.buy_a_drink(self.coffee_shop, self.drink1)
        self.assertEqual(self.customer.wallet, 47.50)
        self.assertEqual(self.coffee_shop.till, 202.50)
