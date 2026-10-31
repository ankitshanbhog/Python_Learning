def execution_logger(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function Completed")
        return result
    return wrapper


@execution_logger
def calculate_area(length,width):
    return length * width

@execution_logger
def introduction(name):
    return f"Hello {name}"

answer = calculate_area(10,20)
print(answer)

answer = introduction("Alex")
print(answer)