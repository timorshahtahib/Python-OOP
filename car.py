from turtle import color


class car:
    color="red"
    
    def getcolor(self,color):
  
        self.color=color
        return   self.color  
     

myob=car()


print(myob.getcolor("golsd"))