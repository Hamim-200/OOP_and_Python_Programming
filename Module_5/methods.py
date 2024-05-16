def call():
    print('Calling someone')
    return 'call done'

class Phone:
    price = 1200
    color = 'Blue'
    brand = 'Samsung'
    features = ['Camera','Speaker']

    def call(self):
        print('Calling one person')

    def send_sms(self,phone,sms):
        text = f'Sending sms to :{phone} and message : {sms}'
        return text        

my_phone = Phone()
print(my_phone.features)
my_phone.call()
result = my_phone.send_sms(41524, 'How are you?')
print(result)