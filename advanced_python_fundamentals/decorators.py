
def my_decorator(func):
    def wrapper():
        print("BEfore the function")
        func()
        print("After the Function")

    return wrapper


@my_decorator
def greet():
    print("hello")

greet()