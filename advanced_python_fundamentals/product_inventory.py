class inventory:
    store_name = "My-Store"
    
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @staticmethod
    def isvalidPrice(price):
        if price > 0:
            return True
        return False

    @classmethod
    def change_store_name(cls,new_name):
        cls.store_name = new_name

    @property
    def total_value(self):
        value = self.price * self.quantity
        return value

 
p1 = inventory("Laptop", 50000, 3)
p2 = inventory("Mouse", 500, 10)
p3 = inventory("Keyboard", 2000, 2)
p4 = inventory("Monitor", 15000, 4)

products = [p1, p2, p3, p4]

def low_stock_products(products):
    for product in products:
        if product.quantity < 5:
            yield product

inventory.change_store_name("Tech World")

print(p1.store_name)
print(p2.store_name)

print(p1.total_value)


def operation_logger(func):
    def wrapper(*args, **kwargs):
        print("Inventory Operation Started ...")
        result = func(*args, **kwargs)
        print("Inventory Operation Succesfull")
        return result
    return wrapper

@operation_logger
def add_product(products, product):
    products.append(product)
    print(f"{product.name} added successfully")

p5 = inventory("Headphones", 3000, 6)
add_product(products, p5)