from index import BankAccount, Bank 


barclays = Bank()

account1 = BankAccount("Christopher", "1234567890", 900000)
barclays.add_account(account1)
account1.deposit(1000)
account1.get_balance()
account1.withdraw(500)
account1.get_balance()

account2 = BankAccount("Feisal", "0987654321", 500000)
barclays.add_account(account2)
account2.get_balance()
account2.withdraw(1000)
account2.get_balance()

barclays.remove_account("1234567890")