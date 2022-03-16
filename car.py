

class car:
    def __init__(self,color,model=1992):
        self.color=color
        self.model=model
        
        
    def getModel(self):
        return self.model
    def getcolor(self):
  
        return   self.color  
     

myob=car("red",1990)


print(myob.getcolor())
print(myob.getModel())