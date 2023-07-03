# To add the deposit to slot machine
def deposit():
    while True:
        amount = input("Enter Your Amount :₹")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0")
        else:
            print("Please enter a number. ")
    
    return amount

deposit()