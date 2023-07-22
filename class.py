class dog:
    dogname = ""
    dogage = ""
    dogcotcolor = ""
    def description(self):
        print(self.dogname)
        print(self.dogage)
    def get_info(self):
        print(self.dogcotcolor)
class JackRussellTerrier(dog):
    breed = ""
    def breed(self):
        print(self.breed)
class Bulldog(JackRussellTerrier):
    def fun(self):
        print("Name of the dog is:",self.dogname)
        print("Age of the dog is:",self.dogage )
        print("Cot color of the dog is:",self.dogcotcolor)
        print("Price of the dog is:",self.dogbreed)
obj = Bulldog()  
obj.dogname = "bull"
obj.dogage = 12
obj.dogcotcolor = "red"
obj.dogbreed = "preshian"
obj.fun()  



        