registered = {"A12", "B14", "C16"}
incoming = ["B14", "D18", "A12", "D18", "E20"]

incoming_unique = set(incoming)
print(incoming_unique)

print(registered & incoming_unique)
print(incoming_unique-registered)

registered.update(incoming_unique)
print(registered)
print(len(registered))