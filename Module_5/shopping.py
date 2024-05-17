class Shopping:
    def __init__(self,name):
        self.name=name
        self.cart = []

    def add_to_cart(self,item,price,quantity):
        product = {'item ': item,'price': price,'Quantity':quantity}
        self.cart.append(product)

    def checkout(self,amount):
        total = 0 
        for item in self.cart:
            # print(item)
            total += item['price'] * item['Quantity']
        print('Total Price',total)
        if amount <total:
            print(f'Please provide {total-amount} more')
        else:
            extra = amount - total
            print(f'Here is your items and extra money{extra}')    


nisho = Shopping ('Nisho Khan')
nisho.add_to_cart('alu',50,6)
nisho.add_to_cart('egg',10,24)
nisho.add_to_cart('rice',80,2)
print(nisho.cart)
nisho.checkout(900)