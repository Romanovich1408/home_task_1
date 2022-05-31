    # home task lesson_1
class Product:
    """
    Describes products
    """
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f"{self.title}: {self.price} грн."

class Customer:
    
    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __str__(self):
        return f"{self.surname} {self.name[0]}., {self.phone}"

class Order:
    
    def __init__(self, customer: Customer, products = None):
        self.customer = customer
        self.products = products

    def __str__(self):
        res = "\n".join(map(str, self.__products))
        return f"{self.customer}\n{res}\nTotal price: {self.total_price()} грн"

    def add_product(self, value: Product):
        if isinstance(value, Product):
            self.__products.append(value)
        
    def remove_propuct(self, value):
         if value in self.__products:
             self.__products.remove(value)

    def total_price(self):
        s = 0
        for item in self.products:
            s += item.price
        return s


if __name__ == "__main__":
    x = Product("apple", 23)
    y = Product("banana", 25)
    z = Product("orange", 23)

    customer_1 = Customer("Ivan", "Ivanov", "0950000000")
    customer_2 = Customer("Petr", "Petrov", "0990000000")

    order_1 = Order(customer_1, [x, y, y, y, z])
    order_2 = Order(customer_2, [x,z])


    print(order_1)
    print(order_2)
