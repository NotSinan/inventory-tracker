from item import Item

class Inventory:
    def __init__(self) -> None:
        self.items = []

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def remove_item(self, item: Item) -> None:
        self.items.remove(item)

    def list_items(self) -> None:
        for item in self.items:
            print(item)
    
    def search_item(self, name: str) -> Item:
        for item in self.items:
            if item.name == name:
                return item
        return None
    
    def update_quantity(self, name: str, new_quantity: int) -> None:
        item = self.search_item(name)
        if item is not None:
            item.update_quantity(new_quantity)
    
    def update_price(self, name: str, new_price: float) -> None:
        item = self.search_item(name)
        if item is not None:
            item.update_price(new_price)


