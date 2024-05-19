class Company:
    def __init__(self,name,address,) -> None:
        self.name = name
        self.bus = []
        self.routes = []
        self.drivers = []
        self.counter = []
        self.manager = []
        self.supervisor = []

class Driver:
    def __init__(self,name,licence,age) -> None:
        self.licence = licence
        self.name = name
        self.age = age
        