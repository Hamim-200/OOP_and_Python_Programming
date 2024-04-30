balance = 3000

def buy_things(item,price):
    global balance
    print(f'Previous balance value',balance)
    balance = balance - price
    print(f'Balance After buy {item} ',balance)

buy_things('Sunglass',1000)
