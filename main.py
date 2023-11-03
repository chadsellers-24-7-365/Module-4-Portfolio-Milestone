class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)

        """
        Initializes the ItemToPurchase class with the specified attributes.
        
        Args:
            item_name (str): The name of the item.
            item_price (float): The price of the item.
            item_quantity (int): The quantity of the item.
        """
    def print_item_cost(self):
        """
        Prints the cost of the item.

        Returns:
            float: The total cost of the item.
        """
        item_total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${item_total_cost}")
        return item_total_cost


# Example usage:
if __name__ == "__main__":
    item1 = ItemToPurchase()
    print("Item 1")
    item1.item_name = input("Enter the item name: ")
    item1.item_price = float(input("Enter the item price: "))
    item1.item_quantity = int(input("Enter the item quantity: "))

    item2 = ItemToPurchase()
    print("\nItem 2")
    item2.item_name = input("Enter the item name: ")
    item2.item_price = float(input("Enter the item price: "))
    item2.item_quantity = int(input("Enter the item quantity: "))

    print("\nTOTAL COST")
    total_cost = item1.print_item_cost() + item2.print_item_cost()
    print(f"Total: ${total_cost}")
