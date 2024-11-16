
class ShoppingCart(object):

    def __init__(self, customer_name="none", current_date="January 1, 2020"):

        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, itemName):
        found = False
        for item in self.cart_items:
            if item.item_name == itemName:
                self.cart_items.remove(item)
                found = True

        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, ItemToPurchase):
        found = False
        for item in self.cart_items:
            if item.item_name != None:
                if item.item_name == ItemToPurchase.item_name:
                    # defaults
                    # self.item_name = "none"
                    # self.item_price = 0.00
                    # self.item_quantity = 0
                    # self.item_description = "none"
                    if item.item_quantity != 0:
                        item.item_quantity = ItemToPurchase.item_quantity
                    if item.item_price != 0.00:
                        item.item_price = ItemToPurchase.item_price
                    if item.item_description != "none":
                        item.item_description = ItemToPurchase.item_description
                    found = True

        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items += item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        total_cost = 0.0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return round(total_cost, 2)

    def print_total(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"Number of Items: {self.get_num_items_in_cart()}\n")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"\nTotal: ${round(self.get_cost_of_cart(),2)}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

