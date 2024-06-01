class Person:
    def __init__(self,name,age,height,weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print('Vat dal mach')

class Cricketer(Person):
    def __init__(self, name, age, height, weight,team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    # OVERRIDE
    def eat(self):
        print('Vegetables')

    # + Sign operator overload
    def __add__(self,other):
        return self.age + other.age
    
    # * Sign operator overload
    def __mul__(self,other):
        return self.age * other.age

sakib = Cricketer('Sakib',38,68,91,'BD')
mushi = Cricketer('Mushi',40,61,81,'BD')
# sakib.eat()





print(45+64)
print('Sakib'+ 'Rakib')
print([12,98] + [5,6,7,3,2])
print(sakib+mushi)
print(sakib*mushi)