products = {
    "apple": 100,
    "banana": 40,
    "milk": 60
}

item = input("Enter product name: ").lower()

if item in products:
    print("Price of", item, "is", products[item])
else:
    print("Product not found")
