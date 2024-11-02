from ItemToPurchase import ItemToPurchase
def main():
    itemsToPurchase = 2
    itemsPurchased = 0
    itemsPurchasedHolder = []
    while itemsPurchased < itemsToPurchase:
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

        itemsPurchased += 1
        item.print_item_cost()
        itemsPurchasedHolder.append(item)
        print()

    print("TOTAL COST")
    total = 0
    for item in itemsPurchasedHolder:
        total += round(item.item_price * item.item_quantity, 2)
        item.print_item_cost()

    print(f"\nTotal: ${total:.2f}")

if __name__ == '__main__':
    main()
