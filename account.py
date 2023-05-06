class Account:
    bank_name = "Barclays"
    def __init__(self,account_number,account_name,balance):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance
        
    def deposit(self,amount):
        self.balance+=amount
        return f"{self.account_name} your balance is {self.balance}"
    
    def withdraw(self,amount):
        self.balance -=amount
        return f"{self.account_name} your {self.bank_name} acount has {self.balance} euros"
    def check_balance(self):
        return f"Hello {self.account_name} your {self.account_number} has {self.balance}"