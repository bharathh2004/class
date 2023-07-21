class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age        
class JackRussellTerrier(dog):
    def __init__(self,name,age,cot_color):
        super().__init__(name,age) 
        self.cot_color = cot_color
class Bulldog(JackRussellTerrier):
    def __init__(self,name,age,cot_color,price):
        super().__init__(name,age,cot_color)
        self.price = price
    def fun(self):
        print("Name of the dog is:",self.name)
        print("Age of the dog is:",self.age )
        print("Cot color of the dog is:",self.cot_color)
        print("Price of the dog is:",self.price)
obj = Bulldog('pershian',12,'RED',12000)  
obj.fun()          




        