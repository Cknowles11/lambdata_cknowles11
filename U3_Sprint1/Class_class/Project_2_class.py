class Bank_account():

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, money):
        print(self.balance + money)

    def withdrawal(self, money):
        print(self.balance - money)


if __name__=="__main__":
    new_balance = Bank_account(100)
    new_balance.deposit(100)