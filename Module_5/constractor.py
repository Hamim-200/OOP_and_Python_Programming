class Phone:
    manufactured = 'China'

    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price 
        

    def send_sms(self,phone,sms):
        text = f'Sending sms to :{phone} and message : {sms}'
        print(text ) 

my_phone = Phone('Mark' , 'Oppo',9800)
print(my_phone.owner,my_phone.brand,my_phone.price)

her_phone = Phone('Rober','Iphone',98342)
print(her_phone.owner,her_phone.brand,her_phone.price)

her_phone.send_sms()
