cart = []

cart.append("Laptop")
cart.append("Mouse")
cart.append("Keyboard")

print("Cart:", cart)

cart.remove("Mouse")

print("After removing Mouse:", cart)

item = input("Enter item to search: ")

if item in cart:
    print("Item is available")
else:
    print("Item is not available")

print("Shopping Cart:", cart)

print("Total items:", len(cart))

