# Task 9: Implement a simple banking system. Create a BankAccount class that
# allows for deposits and withdrawals, and keeps track of the current balance. 
# Ensure that the account cannot go below $0.

class BankAccount:

    # initialized balance
    def __init__(self, balance):
        self.balance = balance

    def balance_def(self):
        number = format(self.balance, ".2f")
        print(f"Your current balance is R{number}")

    # deposit adds amount to balance
    def deposit(self):
        try:
          deposit = float(input("How much do you want to deposit: R"))
          self.balance = self.balance + deposit    
        except:
          print('An exception occurred. Please try again.')
    
    # withdraw subtracts amount from balance
    # can go beyond 0
    def withdraw(self):
        try:
            amountWithdraw = float(input("How much do you want to withdraw: R"))
            if (self.balance - amountWithdraw) > 0:
                self.balance = self.balance - amountWithdraw
            else:
                print("You have insufficient balance.")
        except:
          print('An exception occurred. Please try again.')


if __name__ == "__main__":

    balance = 0.00
    bank = BankAccount(balance)
    bankOn = True

    # Keeps the banks running until otherwise
    # used try to catch all errors
    
    while bankOn:
        bank.balance_def()
        print("1. Deposit"+"\n"
              "2. Withdraw"+"\n"
              "3. Quit")
        try:
            status = int(input("what do you want to do.(Select a number): "))
            if status == 1:
               bank.deposit()
            elif status == 2:
               bank.withdraw()
            elif status == 3:
               bank.balance_def()
               print("Goodbye")
               bankOn = False
            else:
               print("Select a valid choice (Select a number)")
               continue
        except:
          print('An exception occurred. Please try again.')
        
        

