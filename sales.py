from inventory import Inventory
from sale import Sale

class Sales:
    def __init__(self, inventory: Inventory) -> None:
        self.inventory = inventory
        self.sales = []
    
    def make_sale(self, item_name, quantity):
        item = self.inventory.search_item(item_name)
        if item is not None and item.quantity >= quantity:
            item.update_quantity(-quantity)
            total_price = quantity * item.price
            sale = Sale(item.name, quantity, total_price)
            self.sales.append(sale)
            return total_price
        else:
            print("Quantity low.")
            return None
        
    def get_total_sales(self):
        sum_of_sales = 0
        for sale in self.sales:
            sum_of_sales += sale.total_price
        return sum_of_sales
    
    def list_sales(self):
        for sale in self.sales:
            print(f"{sale.item_name}, {sale.quantity}, {sale.total_price}")

        


        