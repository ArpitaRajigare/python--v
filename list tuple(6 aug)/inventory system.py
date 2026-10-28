inventory = {}

def add_product():
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    inventory[name] = quantity
    print("Product added successfully.")

def update_product():
    name = input("Enter product name: ")
    if name in inventory:
        quantity = int(input("Enter new quantity: "))
        inventory[name] = quantity
        if inventory[name] == 0:
            remove_product(name)
        print("Product updated successfully.")
    else:
        print("Product not found.")

def remove_product(name=None):
    if name is None:
        name = input("Enter product name: ")
    if name in inventory:
        del inventory[name]
        print("Product removed successfully.")
    else:
        print("Product not found.")

def analyze_inventory():
    if inventory:
        product = max(inventory, key=inventory.get)
        print("Product with highest stock:", product)
        print("Quantity:", inventory[product])
    else:
        print("Inventory is empty.")

    print("Total number of unique products:", len(inventory))

while True:
    print("\n1. Add Product")
    print("2. Update Product")
    print("3. Display Product with Highest Stock")
    print("4. Remove Product")
    print("5. Display Total Unique Products")
    print("6. Display Inventory")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        update_product()

    elif choice == "3":
        analyze_inventory()

    elif choice == "4":
        remove_product()

    elif choice == "5":
        print("Total number of unique products:", len(inventory))

    elif choice == "6":
        print("Inventory:", inventory)

    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
