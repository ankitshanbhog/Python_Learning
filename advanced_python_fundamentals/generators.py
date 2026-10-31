def get_numbers():
    yield 10
    yield 20 
    yield 30

numbers = get_numbers()

print(next(numbers))
