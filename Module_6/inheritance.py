class Device:
        def __init__(self,brand,price,color,origin) -> None:
            self.brand = brand
            self.price = price
            self.color = color
            self.origin = origin


class Laptop:
    def __init__(self,memory) ->None:
        self.memory = memory

    def run(self):
        return f'Running laptop : {self.brand}'
    
    def codeing(self):
        return f'Learning Python'

class Phone(Device):
    def __init__(self,brand,price,color,origin,dual_sim) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand,price,color,origin)

    def phone_call(self,number,text):
        return f'Sending SMS to : {number} with: {text}'
    
    def __repr__(self) -> str:
        return f'My New Phone: {self.brand} {self.color} {self.dual_sim}'

class Watch:
    def __init__(self,release_year) -> None:
        self.release_year = release_year

    def what_time(self,day,year):
        return f'The day is : {day} and the year is: {year}'
    


my_phone = Phone('Iphone',293453,'silver','China',True)
print(my_phone.brand)
print(my_phone)