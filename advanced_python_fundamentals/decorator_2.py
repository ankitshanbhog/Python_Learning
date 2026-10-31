def my_decorator(func):
    def wrapper():
        print("Starting Calculation")
        func()
        print("Calculation Finished")

    return wrapper


@my_decorator
def calculate():
    print("Calculating 10 + 20")

calculate()