class UserName:
    def __init__(self, username, email, uId):
        self.username = username
        self.email = email
        self.uId = uId
        
    def display(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"User ID: {self.uId}")
        

userOne = UserName("Mohammad Abdullah", "abdullah917828@gmail.com", 202322240356)
userOne.display()