class Number:
    a = 10
    
    @classmethod
    def showNumber(self): #* you should write here self argument or cls it dose not any meter 
        print("Number:", self.a)
        

A = Number()
A.a = 40
A.showNumber()