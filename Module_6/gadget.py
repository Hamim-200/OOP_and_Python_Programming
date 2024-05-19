class Laptop:

    def __init__(self,brand,price,color,memory) ->None:
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory

    def run(self):
        return f'Running laptop : {self.brand}'
    
    def codeing(self):
        return f'Learning Python'

class Phone:
    def __init__(self,brand,price,color,dual_sim) -> None:
        self.brand= brand
        self.price = price
        self.color = color
        self.dual_sim = dual_sim

    def phone_call(self,number,text):
        return f'Sending SMS to : {number} with: {text}'

class Watch:
    def __init__(self,brand,price,color,release_year) -> None:
        self.brand= brand
        self.price = price
        self.color = color
        self.release_year = release_year

    def what_time(self,day,year):
        return f'The day is : {day} and the year is: {year}'