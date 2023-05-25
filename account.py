class Account:
    bank_name = "Barclays"
    def __init__(self,account_number,account_name,balance):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0
        
        
        
    def deposit(self,amount):
        self.balance+=amount
        return f"{self.account_name} your balance is {self.balance}"
    
    def withdraw(self,amount):
        self.balance -=amount
        return f"{self.account_name} your {self.bank_name} acount has {self.balance} euros"
    def check_balance(self):
        return f"Hello {self.account_name} your {self.account_number} has {self.balance}"
    
class BankAccount:
    def __init__(self):
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        transaction = {
            "amount": amount,
            "narration": "deposit"
        }
        self.deposits.append(transaction)
    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            transaction = {
                "amount": amount,
                "narration": "withdrawal"
            }
            self.withdrawals.append(transaction)
        else:
            print("Insufficient balance!")

    def print_statement(self):
        transactions = self.deposits + self.withdrawals
        for transaction in transactions:
            print(f"{transaction['narration']} - {transaction['amount']}")

    def borrow_loan(self, amount):
        if self.loan_balance == 0 and amount > 100 and len(self.deposits) >= 10:
            total_deposits = sum(transaction['amount'] for transaction in self.deposits)
            if amount <= total_deposits / 3:
                self.loan_balance += amount
                print("Loan approved!")
            else:
                print("Loan amount exceeds 1/3 of total deposits!")
        else:
            print("Loan request rejected!")

    def repay_loan(self, amount):
        if self.loan_balance > 0:
            if amount >= self.loan_balance:
                self.balance += (amount - self.loan_balance)
                self.loan_balance = 0
                print("Loan fully repaid!")
            else:
                self.loan_balance -= amount
                print("Partial loan repayment made!")
        else:
            print("No outstanding loan!")

    def transfer(self, amount, destination_account):
        if self.balance >= amount:
            self.balance -= amount
            destination_account.deposit(amount)
            print("Transfer successful!")
        else:
            print("Insufficient balance!")