class Account:
    # Construct an Account object
    def __init__(self, id, currentBalance=0, savingsBalance=0, annualInterestRateSavings=3.4):
        self.id = id
        self.currentBalance = currentBalance
        self.savingsBalance = savingsBalance
        self.annualInterestRateSavings = annualInterestRateSavings

    def getId(self):
        return self.id

    def currentAccountBalance(self):
        return self.currentBalance

    def withdrawCurrentAccount(self, amount):
        self.currentBalance -= amount

    def depositCurrentAccount(self, amount):
        self.currentBalance += amount

    def transferCurrentAccount(self, amount):
        self.currentBalance += amount
        self.savingsBalance -= amount

    def savingsAccountBalance(self):
        return self.savingsBalance

    def withdrawSavingsAccount(self, amount):
        self.savingsBalance -= amount

    def depositSavingsAccount(self, amount):
        self.savingsBalance += amount

    def transferSavingsAccount(self, amount):
        self.savingsBalance += amount
        self.currentBalance -= amount

    def savingsAccountMonthlyInterest(self):
        return self.savingsBalance * self.savingsAccountMonthlyInterest()

    def savingsAccountAnnualInterestRate(self):
        return self.annualInterestRateSavings

    def savingsAccountMonthlyInterestRate(self):
        return self.annualInterestRateSavings / 12
                    
