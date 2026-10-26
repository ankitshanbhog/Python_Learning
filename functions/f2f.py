def square(n):
    return n*n

def apply_operation(number,operation):
    return operation(number)

print(apply_operation(5,square))