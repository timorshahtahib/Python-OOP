import re


class Point:
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
      
    def __str__(self):
        
        return "Point x={}, Point Y={}".format(self.a,self.b)
    
    
    


p=Point(12,13)
print(p)