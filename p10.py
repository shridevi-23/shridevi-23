def withdraw(account,amount):
    if amount>account['balance']:
        print("Insufficient funds!")
    else:
        account['balance'] -=amount
        account['transaction'].append(f"withdrawal:${amount}")
        print(f"withdrawal successful.Remaining balance['balance'])")
        
def deposit(account,amount):
    account['balance']+=amount
    account['transactions'].append(f"Deposit:${amount}")
    print(f"Deposit successful.Remaining balance:${account['balance']}")
    
def get_balance(account):
    return account['balance']

def get_transaction_history(account):
    return account['transactions']