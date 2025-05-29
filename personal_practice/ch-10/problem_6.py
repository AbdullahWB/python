from random import randint

class Train:
    def __init__(abdullah, trainNo):
        abdullah.trainNo = trainNo
        
    def bookTik(self, name, lFrom, lTo):
        print(f"Train is {self.trainNo} and passenger is {name} who go from {lFrom} to {lTo}")
        
    def getStatus(self):
        print(f"Train {self.trainNo} is currently running")
    
    def getFair(self, lFrom, lTo):
        print(f"train {self.trainNo} ticket fare is from {lFrom} to {lTo} is {randint(1111, 9999)}")
        

t = Train(547554)
t.bookTik("Mohammad Abdullah","dhaka", "chittagong")
t.getFair("dhaka", "chittagong")
t.getStatus()
