class circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        a=self.r*self.r*22/7
        return('The area is',a)
    def per(self):
        p=self.r*2*22/7
        return('The perimeter is',p)
O1=circle(int(input('Enter the radius: ')))
print(O1.area(),O1.per())