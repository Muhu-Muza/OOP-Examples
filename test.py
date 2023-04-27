from index import BankAccount, Bank 


# barclays = Bank()

# account1 = BankAccount("Christopher", "1234567890", 900000)
# barclays.add_account(account1)
# account1.deposit(1000)
# account1.get_balance()
# account1.withdraw(500)
# account1.get_balance()

# account2 = BankAccount("Feisal", "0987654321", 500000)
# barclays.add_account(account2)
# account2.get_balance()
# account2.withdraw(1000)
# account2.get_balance()

# barclays.remove_account("1234567890")




# Create two banks
tanbic_bank = Bank("Tanbic")
zcb_bank = Bank("ZCB")

tanbic_bank.get_name()
dtb_bank.get_name()

# Create three accounts for Tanbic bank and add them
account1 = BankAccount("Christopher", "1234567890", 900000)
account2 = BankAccount("Muhumuza", "7493748002", 100000)
account3 = BankAccount("Babu", "0859376203", 2500000)

tanbic_bank.add_account(account1)
tanbic_bank.add_account(account2)
tanbic_bank.add_account(account3)


# Create three accounts for DTB bank and add them
account4 = BankAccount("Laura", "0849387094", 750000)
account5 = BankAccount("Alvin", "2654738005", 2000000)
account6 = BankAccount("Tina", "0084736256", 5000000)

dtb_bank.add_account(account4)
dtb_bank.add_account(account5)
dtb_bank.add_account(account6)

# Retrieve an account from Tanbic bank using its account number
account = tanbic_bank.get_account("7493748002")

# Remove an account from DTB bank using its account number
dtb_bank.remove_account("2654738005")