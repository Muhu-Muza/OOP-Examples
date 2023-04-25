"""
Create a class called BankAccount that encapsulates information about a bank account, 
such as the account holder's name, account number, and balance. 
The class should have methods for depositing money, withdrawing money, and checking the account balance. 
Ensure that the balance cannot be accessed or modified outside the class. 
Use encapsulation to ensure that the data of the BankAccount object is secure.
Create a class called Bank that should hold the accounts being created

"""


class Bank:
    def __init__(self):
        self.__accounts = {}

    def add_account(self, account):
        self.__accounts[account.get_account_number()] = account
        print("Account added successfully")

    def get_account(self, account_number):
        if account_number in self.__accounts:
            return self.__accounts[account_number]
        else:
            print("Account not found")

    def remove_account(self, account_number):
        if account_number in self.__accounts:
            del self.__accounts[account_number]
            print("Account removed successfully")
        else:
            print("Account not found")
        

class BankAccount:
    def __init__(self, acc_name, acc_number, balance=0):
        self.__acc_name = acc_name
        self.__acc_number = acc_number
        self.__balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("Cannot process this deposit, please deposit an amount greater than 0")
        else:
            self.__balance += amount
            print(f"Cash deposit of {amount} Successful. Your new balance is {self.__balance}.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Not enough funds to complete the transaction !")
        elif amount <= 0:
            print("Please enter a valid amount to withdraw.")
        else:
            self.__balance -= amount
            print(f"Your account has been debited with {amount}. Your new balance is {self.__balance}.")

    def get_balance(self):
        print(f"Your account balance is {self.__balance}.")

    def get_account_number(self):
        return self.__acc_number

"""

Create a class called Rectangle that represents a rectangle object. 
The class should have attributes for the length and width of the rectangle 
and methods for calculating the area and perimeter of the rectangle. 
Then create a subclass called Square that inherits from Rectangle 
and has a method for calculating the diagonal length of the square. 
Ensure that the length and width of the square are always equal by overriding the parent class's 
methods for setting the length and width attributes.

"""
import math

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    
    def area(self):
        return self.__length * self.__width
    
    def perimeter(self):
        return 2 * (self.__length + self.__width)
    
    def set_length(self, length):
        self.__length = length
    
    def set_width(self, width):
        self.__width = width

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def diagonal(self):
        return math.sqrt(2) * self.__length
    
    def set_length(self, side):
        self.__length = side
        self.__width = side
    
    def set_width(self, side):
        self.__width = side
        self.__length = side
