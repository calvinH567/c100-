from sqlite3 import complete_statement


class Car(object):
    def __init__(self,color,speed,model,company,seats):
        self.color=color
        self.speed=speed
        self.model=model
        self.company=company
        self.seats=seats
    def StartCar(self):
        print("car Start",self.model)

        
Tesla=Car('red',100,5,"Tesla",4)
Tesla.StartCar()