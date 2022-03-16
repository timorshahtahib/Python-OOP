class animal:
    
    
    
 def __init__(self,name):
      self.name=name
        
        
def getName(self):
    
    return self.name
    
def run(self):
    return "{} is rum ".format(self.name)


class bird(animal):
    
    def dance(self):
     return"{} is dance".format(self.name)
    
class animalFlay:
    def  fly(self):
        return "{} is fly".format(self.name)
    
class parror(bird,animalFlay):
    
    def swim(self):
        return("{} is  swim".format(self.name))
        



p1=parror("parrot")

print(p1.dance())
print(p1.swim())