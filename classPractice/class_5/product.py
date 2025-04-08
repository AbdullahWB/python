class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def is_in_stock(self):
        if self.stock > 0:
            return f"we have so so stock {self.stock}"
        else:
            return "we are out of stock"
        
    def update_stock(self, quantity):
        self.stock += quantity
        return f"stock updated successfully. new stock is {self.stock}"
    
    def gef_product_details(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Stock: {self.stock}"
    

product1 = Product(1, "Laptop", 1000, 5)
print(product1.is_in_stock())
product1.update_stock(10)
print(product1.is_in_stock())
print(product1.get_product_details())
