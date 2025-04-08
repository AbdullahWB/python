from cartClass import Cart

class User:
    def __init__(self, user_id, name, email, pId, pd, qu):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.cart = Cart(pId, pd, qu)
        
    def view_cart(self):
        return self.cart.display_cart()
    
    def checkout(self):
        return self.cart.checkout()
    
    def add_item(self, item, quantity):
        self.cart.add_product(item, quantity)
        

user1 = User(1, "John Doe", "johndoe@example.com", 1, "product4", 5)

user1.add_item("Shirt", 3)

print(user1.view_cart())