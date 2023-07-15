import unittest
from ATM import Account

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account(1, currentBalance=100, savingsBalance=200, annualInterestRateSavings=3.4)

    def test_getId(self):
        self.assertEqual(self.account.getId(), 1)

    def test_currentAccountBalance(self):
        self.assertEqual(self.account.currentAccountBalance(), 100)

    def test_withdrawCurrentAccount(self):
        self.account.withdrawCurrentAccount(50)
        self.assertEqual(self.account.currentAccountBalance(), 50)

    def test_depositCurrentAccount(self):
        self.account.depositCurrentAccount(50)
        self.assertEqual(self.account.currentAccountBalance(), 150)

    def test_transferCurrentAccount(self):
        self.account.transferCurrentAccount(50)
        self.assertEqual(self.account.currentAccountBalance(), 150)
        self.assertEqual(self.account.savingsAccountBalance(), 150)

    def test_savingsAccountBalance(self):
        self.assertEqual(self.account.savingsAccountBalance(), 200)

    def test_withdrawSavingsAccount(self):
        self.account.withdrawSavingsAccount(50)
        self.assertEqual(self.account.savingsAccountBalance(), 150)

    def test_depositSavingsAccount(self):
        self.account.depositSavingsAccount(50)
        self.assertEqual(self.account.savingsAccountBalance(), 250)

    def test_transferSavingsAccount(self):
        self.account.transferSavingsAccount(50)
        self.assertEqual(self.account.savingsAccountBalance(), 250)
        self.assertEqual(self.account.currentAccountBalance(), 150)

    def test_savingsAccountMonthlyInterest(self):
        self.assertAlmostEqual(self.account.savingsAccountMonthlyInterest(), 6.876712328767123, places=14)

    def test_savingsAccountAnnualInterestRate(self):
        self.assertEqual(self.account.savingsAccountAnnualInterestRate(), 3.4)

    def test_savingsAccountMonthlyInterestRate(self):
        self.assertAlmostEqual(self.account.savingsAccountMonthlyInterestRate(), 0.2833333333333333, places=14)

if __name__ == '__main__':
    unittest.main()
