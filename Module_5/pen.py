class Pen:
     def __init__(self,name,brand,price,color,country):
        self.name=name
        self.brand = brand
        self.price = price
        self.color = color
        self.country = country

pen_one= Pen('Pen_one','Matador',10,'Red','Banglades')
print(pen_one.name,pen_one.brand,pen_one.price,pen_one.color,pen_one.country) 
