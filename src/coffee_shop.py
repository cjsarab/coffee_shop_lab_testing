class CoffeeShop:
    
    def __init__(self, name, till, stock):
        self.name = name
        self.till = till
        
        self.stock = stock

    def increase_till(self, amount):
        self.till += amount

    
    def get_total_stock_value(self):
        total_stock_price=0
        for stock_item in self.stock:
            total_stock_price += stock_item["price"] * stock_item["total"]
        return(total_stock_price)


    def get_stock_value_of_drinks(self):
        total_stock_price=0
        for stock_item in self.stock:
            if stock_item["type"]== "drink":
                total_stock_price += stock_item["price"] * stock_item["total"]
        return(total_stock_price)
    
    