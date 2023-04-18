class Item:
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name} - {self.price} - {self.quantity} in stock."

    def update_price(self, new_price: float) -> None:
        self.price = new_price

    def update_quantity(self, quantity_change: int) -> None:
        self.quantity += quantity_change
    
