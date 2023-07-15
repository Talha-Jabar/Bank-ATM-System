import random
import time
from ATM import Account

def main():
    # Creating accounts
    accounts = []
    for i in range(1000, 9999):
        account = Account(i, 0)
        accounts.append(account)

    while True:

        # Reading id from user
        print("Welcome to International Bank.")
        id = int(input("\nEnter 4-digit account pin: "))

        # Loop till id is valid
        while id < 1000 or id > 9999:
           id = int(input("\nInvalid Id.. Re-enter: "))

        # Iterating over interface
        while True:

            # Printing menu
            print("\nHow can we help you today?")
            print("""\n1 - View Current Balance \t\t2 - Withdraw Current \n3 - Deposit Current \t\t\t4 - Transfer from Saving to Current Account
                    \n5 - View Savings Balance \t\t6 - Withdraw Savings \n7 - Deposit Savings \t\t\t8 - Transfer from Current to Saving Account
                    \n9 - Exit """)

            # Reading selection
            selection = int(input("\nEnter your numerical selection: "))

            # Getting account object
            for acc in accounts:
                # Comparing account id
                if acc.getId() == id:
                    accountObj = acc
                    break

            # View Current Balance
            if selection == 1:
                # Printing balance
                print(
                    f"\nCurrent account balance: ${format(accountObj.currentAccountBalance(), '.2f')} ")
                time.sleep(2)

            # Current Withdraw
            elif selection == 2:
                # Reading amount
                amt = float(
                    input("\nEnter amount to withdraw from current: "))
                ver_current_withdraw = input(
                    f"Is ${format(amt, '.2f')} the correct amount to withdraw, Yes or No ? ")
                ver_current_withdraw = ver_current_withdraw.upper()
                if ver_current_withdraw == "YES":
                    print("\nVerified current account withdraw.")
                    time.sleep(2)
                else:
                    break

                if amt < accountObj.currentAccountBalance():
                    # Calling withdraw method
                    accountObj.withdrawCurrentAccount(amt)
                    # Printing updated balance
                    print(
                        f"Updated current account balance: ${format(accountObj.currentAccountBalance(), '.2f')} ")
                    time.sleep(2)
                else:
                    print(
                        f"\nYour current account balance is less than withdrawl amount: ${format(accountObj.currentAccountBalance(), '.2f')} ")
                    time.sleep(2)

            # Deposit
            elif selection == 3:
                # Reading amount
                amt = float(input("\nEnter amount to deposit in current: "))
                ver_current_deposit = input(
                    f"Is ${format(amt, '.2f')} the correct amount to deposit, Yes or No ? ")
                ver_current_deposit = ver_current_deposit.upper()

                if ver_current_deposit == "YES":
                    # Calling deposit method
                    print("\nVerified current account deposit.")
                    time.sleep(2)
                    accountObj.depositCurrentAccount(amt)
                    # Printing updated balance
                    print(
                        f"\nUpdated current account balance: ${format(accountObj.currentAccountBalance(), '.2f')} ")
                    time.sleep(2)
                else:
                    break

            #Transfer Savings Account to Current Account
            elif selection == 4:
                amt = float(
                    input("\nEnter amount to transfer from savings account to current: "))
                ver_current_transfer = input(
                    f"Is ${format(amt, '.2f')} the correct amount to transfer, Yes or No ? ")
                ver_current_transfer = ver_current_transfer.upper()
                if ver_current_transfer == "YES":
                    print("Verified savings account transfer to current account.")
                    time.sleep(2)
                else:
                    time.sleep(2)
                    break

                if amt < accountObj.savingsAccountBalance():
                    # Calling transfer method
                    accountObj.transferCurrentAccount(amt)
                    # Printing updated balance
                    print(
                        f"Updated current account balance: ${format(accountObj.currentAccountBalance(), '.2f')} ")
                    print(
                        f"Updated savings account balance: ${format(accountObj.savingsAccountBalance(), '.2f')} ")
                    time.sleep(2)
                else:
                    print(
                        f"\nYour savings account balance is less than transfer amount: ${format(accountObj.currentAccountBalance(), '.2f')} ")
                    time.sleep(2)

            # View Saving Balance
            elif selection == 5:
                # Printing balance
                print(
                    f"Savings account balance: ${format(accountObj.savingsAccountBalance(), '.2f')} ")
                time.sleep(2)

            # Savings Withdraw
            elif selection == 6:
                # Reading amount
                amt = float(input("\nEnter amount to withdraw from savings: "))
                ver_savings_withdraw = input(
                    f"Is ${format(amt, '.2f')} the correct amount to withdraw, Yes or No ? ")
                ver_savings_withdraw = ver_savings_withdraw.upper()
                if ver_savings_withdraw == "YES":
                    print("\nVerified savings account withdraw.")
                    time.sleep(2)
                else:
                    time.sleep(2)
                    break
                if amt < accountObj.savingsAccountBalance():
                    # Calling withdraw method
                    accountObj.withdrawSavingsAccount(amt)
                    # Printing updated balance
                    print(
                        f"Updated current account balance: ${format(accountObj.currentAccountBalance(), '.2f')} ")
                    print(
                        f"Updated savings account balance: ${format(accountObj.savingsAccountBalance(), '.2f')} ")
                    time.sleep(2)
                else:
                    print(
                        f"\nYour savings account balance is less than withdrawl amount: ${format(accountObj.savingsAccountBalance(), '.2f')} ")
                    time.sleep(2)

            # Savings Account Deposit
            elif selection == 7:
                # Reading amount
                amt = float(input("\nEnter amount to deposit in savings: "))
                ver_savings_deposit = input(
                    f"Is ${format(amt, '.2f')} the correct amount to deposit, Yes or No ? ")
                ver_savings_deposit = ver_savings_deposit.upper()

                if ver_savings_deposit == "YES":
                    print("\nVerified savings account deposit.")
                    time.sleep(2)
                    # Calling deposit method
                    accountObj.depositSavingsAccount(amt)
                    # Printing updated balance
                    print(
                        f"Updated savings account balance: ${format(accountObj.savingsAccountBalance(), '.2f')} ")
                    time.sleep(2)
                else:
                    break
                    time.sleep(2)

            #Transfer Current Account to Savings Account
            elif selection == 8:
                amt = float(
                    input("\nEnter amount to transfer from current account to savings account: "))
                ver_savings_transfer = input(
                    f"Is ${format(amt, '.2f')} the correct amount to transfer, Yes or No ? ")
                ver_savings_transfer = ver_savings_transfer.upper()
                if ver_savings_transfer == "YES":
                    print("Verified current account transfer to savings account.")
                    time.sleep(2)
                else:
                    break
                if amt < accountObj.checkingAccountBalance():
                    # Calling withdraw method
                    accountObj.transferSavingsAccount(amt)
                    # Printing updated balance
                    print(
                        f"Updated current account balance: ${format(accountObj.currentAccountBalance(), '.2f')} ")
                    print(
                        f"Updated savings account balance: ${format(accountObj.savingsAccountBalance(), '.2f')} ")
                    time.sleep(2)
                else:
                    print(
                        f"\nYour current account balance is less than transfer amount: ${format(accountObj.currentAccountBalance(), '.2f')} ")
                    time.sleep(2)

            elif selection == 9:
                print("\nTransaction is now complete.")
                print("Transaction number: ", random.randint(10000, 1000000))
                print("Current Interest Rate: ",
                      accountObj.annualInterestRateSavings)
                print("Monthly Interest Rate: ",
                      accountObj.annualInterestRateSavings / 12)
                print("Thanks for choosing us as your bank")
                exit()

            # Any other choice
            else:
                print("\nThat's an invalid choice.")
                break

# Main function
main()

  