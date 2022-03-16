import re


class Point:
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
      
    def __str__(self):
        
        return "Point x={}, Point Y={}".format(self.a,self.b)
    
    
    def __add__(self,other):
       a=self.a+other.a
       b=self.b+other.b
       
       return Point(a,b)


p1=Point(12,13)
p2=Point(5,6)


print(p1)
print(p1+p2)