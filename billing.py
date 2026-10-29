print("=== CAMPUS CANTEEN ===")
print("1. Tea - Rs 80")
print("2. Sandwich - Rs 250")
print("3. Juice - Rs 150")
print("4. Coffee - Rs 180")
print("0. Checkout")

total = 0
items = 0

while True:
    choice = input("Choose 1-4, or 0: ")

    if choice == "0":
        break

    if choice == "1":
        name = "Tea"
        price = 80

    elif choice == "2":
        name = "Sandwich"
        price = 250

    elif choice == "3":
        name = "Juice"
        price = 150

    elif choice == "4":
        name = "Coffee"
        price = 180

    else:
        print("Invalid choice.")
        continue

    quantity = int(input("Quantity: "))

    if quantity <= 0:
        print("Enter 1 or more.")
        continue

    line_total = price * quantity

    total += line_total
    items += quantity

    print(f"{quantity} x {name}")
    print(f"Line total: Rs {line_total}")

discount = 0

if total >= 1000:
    discount = total * 0.10

final_total = total - discount

print("\n--- YOUR BILL ---")
print(f"Items: {items}")
print(f"Subtotal: Rs {total}")
print(f"Discount: Rs {discount}")
print(f"To pay: Rs {final_total}")
