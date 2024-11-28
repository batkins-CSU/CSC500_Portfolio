from ItemToPurchase import ItemToPurchase
from ShoppingCart import ShoppingCart
def main():

    complete = False
    name = input("Enter customer's name:\n")
    date = input("Enter today's date as a string:\n")
    print(f"\nCustomer name: {name}")
    print(f"Today's date: {date}")
    shoppingCart = ShoppingCart(customer_name=name, current_date=date)

    while not complete:
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("d - Change item description")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        print()
        choice = input("Choose an option:\n").lower().strip()
        if choice == 'a':
            item = prep_item_for_action()
            shoppingCart.add_item(item)
        elif choice == 'r':
            item_name = input("Enter the item name:\n")
            shoppingCart.remove_item(item_name)
        elif choice == 'c':
            item = prep_item_for_action()
            shoppingCart.modify_item(item)
        elif choice == 'd':
            item = prep_item_for_action()
            shoppingCart.modify_item(item)
        elif choice == 'i':
            shoppingCart.print_descriptions()
        elif choice == 'o':
            shoppingCart.print_total()
        elif choice == 'q':
            complete = True
        else:
            print("Invalid input. Please try again.\n")


def prep_item_for_action():
    item = ItemToPurchase()
    try:
        item.item_name = input("Enter the item name:\n")
    except ValueError:
        print("Invalid input. Please try again.\n")
    try:
        item.item_price = float(input(f"Enter the item price:\n"))
    except ValueError:
        print("Invalid input. Please try again.\n")
    try:
        item.item_quantity = int(input(f"Enter the item quantity:\n"))
    except ValueError:
        print("Invalid input. Please try again.\n")

    try:
        item.item_description = int(input(f"Enter the item description:\n"))
    except ValueError:
        print("Invalid input. Please try again.\n")
    return item


if __name__ == '__main__':
    main()
