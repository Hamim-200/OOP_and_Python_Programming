class User:
    def __init__(self,name,age,money) -> None:
        self._name = name 
        self._age = age
        self.__money = money

    # Getter without any setter is read only attribute
    @property
    def age(self):
        return self._age
    
    @property
    def salary(self):
        return self.__money
    
    @salary.setter
    def salary (self,value):
        if value <0:
            return 'Salary can not be zero'
        self.__money += value

samsu = User('Kopa',21,12000)

# print(samsu.__money)
# print(samsu.age())
print(samsu.age)

# print(samsu.money())
print(samsu.salary)

samsu.salary = 4500
print(samsu.salary)


# Read only --> you cannot set the value. value can not be changed
# getter -->  get a value of a property.most of the time we get the private value.
# setter --> set a value of a property through a method most of the time we will set the value of a private property.