a = {1,2,3,4}
b = {5,6,7,8,1,2,4}

print(a | b)
print(a & b)
print(a - b)
print(a ^ b)



registered = {"A12", "B14", "C16"}
incoming = ["B14", "D18", "A12", "D18"]

for item in incoming:
    registered.add(item)

print(registered)