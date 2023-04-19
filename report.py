from sales import Sales
from inventory import Inventory
class Report:
    def __init__(self, inventory: Inventory, sales: Sales) -> None:
        self.inventory = inventory
        self.sales = sales

    def generate_inventory_report(self):
        print("Inventory Report:\n")
        print(f"{'Name':<15} {'Description':<25} {'Price':<15} {'Quantity':<10}")
        for item in self.inventory.items:
            print(f"{item.name:<15} {item.description:<25} {item.price:<15} {item.quantity:<10}")

    def generate_sales_report(self):
        print("Sales Report:\n")
        for sale in self.sales:
            print(f"{sale.item_name:<15} {sale.quantity:<15} {sale.total_price:<15} {sale.date:<15}")
        