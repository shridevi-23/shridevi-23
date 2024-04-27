def check_username(username):
    # Assuming correct_username is the correct username to be checked against
    correct_username = "user123"
    
    if username == correct_username:
        return True
    else:
        return False

def process_transaction(username, amount):
    if check_username(username):
        # Process the transaction logic here
        print(f"Transaction successful! {amount} units processed for user {username}.")
    else:
        print("Invalid username. Transaction cannot be processed.")

# Example usage:
entered_username = input("Enter your username: ")
transaction_amount = 100  # Example transaction amount

process_transaction(entered_username, transaction_amount)
