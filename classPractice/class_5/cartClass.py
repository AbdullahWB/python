class Cart:
    my_dict = {}
    def __init__(self, cart_id, product, quantity):
        self.cart_id = cart_id
        self.my_dict[product] = quantity
        
    def add_product(self, product, quantity):
        self.my_dict[product] = quantity
        
    def remove_product(self, product):
        del self.my_dict[product]
    
    def calculate_total(self):
        total = 0
        for item in self.my_dict:
            # print(item)
            total += 1
            print("total is: ",total)
            
    def clear_cart(self):
        self.my_dict = {}
        
    def display_cart(self):
        for item in self.my_dict:
            print(f"Product: {item}, Quantity: {self.my_dict[item]}")
            
    def check_cart(self):
        return f"{self.cart_id}, you purchase this product"
        
cart1 = Cart(1, "apple", 2)
cart1.add_product("banana", 3)

print(cart1.my_dict)
cart1.remove_product("apple")
print(cart1.my_dict)
cart1.calculate_total()
cart1.clear_cart()
print(cart1.my_dict)