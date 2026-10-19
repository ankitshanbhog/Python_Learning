items = ["Laptop","Mouse","Keyboard"]

print(items)
print(len(items))

items.append("Monitor")
items.insert(1,"USB Cable")

items.remove("Mouse")

print(items[:3])
print(items[::-1])

print("Keyboard" in items)
items.sort()
print(items)

print(len(items))



