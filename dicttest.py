inventory = {
    "Laptop": 5,
    "Mouse": 12,
    "Keyboard": 7
}

print(inventory)
inventory["Mouse"] = 10
inventory["Monitor"] = 4
print(inventory.get("Laptop"),inventory.get("Tablet",0))

for key,value in inventory.items():
    print(key,value)

unique_products = set(inventory.keys())

print(unique_products)
print(len(unique_products))