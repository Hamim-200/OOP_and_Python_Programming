class Shop:
    shopping_mall = 'Jamuna'

    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = [] #Cart is an instance attributes

    def add_to_cart(self,item):
        self.cart.append(item)

hasan = Shop('Hasan Ali')
hasan.add_to_cart('Shoe')
hasan.add_to_cart('Phone')
hasan.add_to_cart('Laptop')
print(hasan.cart)


nisho = Shop('Nisho')
nisho.add_to_cart('Watch')
nisho.add_to_cart('Cap')
print(nisho.cart)