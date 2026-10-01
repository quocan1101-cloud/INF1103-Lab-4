tax_rate = 0.10

def get_product_name():
    product_name = input("Enter Product Name (or 'quit' to exit): ")
    if product_name == "quit":
        return "quit"

    # Product name must be letters or spaces only
    if not product_name.strip():
        print("Product name cannot be empty.")
        return None
    if not product_name.replace(" ", "").isalpha():
        print("Product name can only contain letters and spaces.")
        return None

    return product_name

def get_quantity():
    quantity_value = input("Enter Quantity: ")

    # Quantity must be a whole number
    try:
        quantity = int(quantity_value)
    except ValueError:
        print("Quantity must be a whole number.")
        return None

    # Quantity must not be negative
    if quantity < 0:
        print("Quantity cannot be negative.")
        return None

    return quantity


def calculate_tax(amount):
    return amount * tax_rate


def load_inventory():
    saved_orders = []
    try:
        with open("orders.txt", "r") as f:
            for line in f:
                if line.strip() != "":
                    number, product_name, quantity, tax = line.strip().split(",")
                    saved_orders.append((number, product_name, quantity, tax))
    except FileNotFoundError:
        pass
    return saved_orders


def save_inventory(orders):
    with open("orders.txt", "a") as f:
        for number, product_name, quantity, tax in orders:
            f.write(f"{number},{product_name},{quantity},{tax}\n")


def generate_report(orders, failed_attempts):
    print("\nAll new orders:")
    for number, product_name, quantity, tax in orders:
        print(f"{number}, {product_name}, {quantity}, Tax: {tax}")
    print(f"Failed input attempts: {failed_attempts}")


def main():
    orders = []
    failed_attempts = 0
    saved_orders = load_inventory()
    order_number = 1001 + len(saved_orders)

    print("Current Orders:")
    print()
    for number, product_name, quantity, tax in saved_orders:
        print(f"{number}, {product_name}, {quantity}, Tax: {tax}")
    print()

    while True:
        product_name = get_product_name()
        if product_name == "quit":
            break
        if product_name is None:
            failed_attempts += 1
            continue

        quantity = get_quantity()
        while quantity is None:
            failed_attempts += 1
            quantity = get_quantity()

        tax = calculate_tax(quantity)

        orders.append((order_number, product_name, quantity, tax))
        print(f"New order added: {order_number}, {product_name}, {quantity}, Tax: {tax}")
        order_number += 1

    save_inventory(orders)
    generate_report(orders, failed_attempts)

    print("\nOrders successfully saved to orders.txt")

main()
