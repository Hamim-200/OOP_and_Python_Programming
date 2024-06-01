class Shopping:
    cart = [] # class attribute / Static attribute
    origin = 'China'

    def __init__(self,name,location) -> None:
        self.name = 'Jamuna' #instance attribute
        self.location = 'Bashundhara'

    def purches(self,item,price,amount):
        reamining = amount - price
        print(f'buying : {item} for price: {price} and remaining: {reamining}')

    @classmethod
    def hudai_dekhi(self,item):
        print('Hudai dekhi but kinbo na',item)


    @staticmethod
    def multiply(a,b):
        result= a*b
        print(result)
# Shopping.purches('A',2,3,4)

# bashundhara = Shopping('Bashundhara','No Location')
# bashundhara.purches('Lungi',500,1000)

# bashundhara.hudai_dekhi('Lungi')
# Shopping.hudai_dekhi('Pant')

Shopping.multiply(4,6)