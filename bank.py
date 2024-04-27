class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.transactions=[]
        
    def withdraw(shetty,amount):
        if amount>shetty.balance:
            print("Insufficient funds!")
        else:
            shetty.balance -=amount
            shetty.transactions.append(f"Withdrawal:${amount}")
            print(f"Withdrawal successsfull.Remaining balance:${shetty.balance}")
            
    def deposit(self,amount):
        self.balance +=amount
        self.transactions.append(f,"Deposit:${amount}")
        print(f"Deposit successful.Remaining balance:${self.balance}")
