
class ItemToPurchase (object):
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.00
        self.item_quantity = 0

    def print_item_cost(self):
        print(f"{self.item_name} {round(self.item_quantity, 2):.2f} for ${round(self.item_price, 2):.2f} each = "
              f"${round(self.item_price * self.item_quantity, 2):.2f}")

