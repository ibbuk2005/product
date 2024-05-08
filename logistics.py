class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Warehouse:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product_name, quantity):
        if product_name in self.inventory:
            self.inventory[product_name].quantity += quantity
        else:
            self.inventory[product_name] = Product(product_name, quantity)

    def update_quantity(self, product_name, new_quantity):
        if product_name in self.inventory:
            self.inventory[product_name].quantity = new_quantity
        else:
            print("Product not found in inventory.")

    def display_inventory(self):
        print("Current Inventory:")
        for product_name, product in self.inventory.items():
            print(f"{product_name}: {product.quantity}")

def main():
    warehouse = Warehouse()

    while True:
        print("\n1. Add Product\n2. Update Quantity\n3. Display Inventory\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            product_name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            warehouse.add_product(product_name, quantity)
        elif choice == "2":
            product_name = input("Enter product name: ")
            new_quantity = int(input("Enter new quantity: "))
            warehouse.update_quantity(product_name, new_quantity)
        elif choice == "3":
            warehouse.display_inventory()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
