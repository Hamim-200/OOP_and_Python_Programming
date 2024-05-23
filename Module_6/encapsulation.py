class Bank:
    def __init__(self,holder_name,initial_deposit,branch) -> None:
        self.holder_name = holder_name #PUBLIC
        self.__balance = initial_deposit #PRIVATE
        self._branch = branch #PROTECTED


    def deposite(self,amount):
        self.__balance +=amount

    def get_balance(self):
        return self.__balance
    
rufsun = Bank('Choto',1000)


print(rufsun.holder_name)
rufsun.deposite(40000)
print(rufsun.get_balance) 