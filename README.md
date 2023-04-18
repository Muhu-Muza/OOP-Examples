# OOP-Examples   
### These examples demonstrate how to use object-oriented programming concepts such as encapsulation and inheritance to create classes that model real-world objects and their behavior   

# Example 1: BankAccount class   
This example demonstrates the creation of a `BankAccount` class, which encapsulates information about a bank account such as the account holder's name, account number, and balance. The class includes methods for depositing money, withdrawing money, and checking the account balance. The data of the BankAccount object is secure, as the balance cannot be accessed or modified outside the class.   

## How to use the BankAccount class   
1. Create an instance of the `BankAccount` class by passing in the account holder's name, account number, and initial balance:   
```
account = BankAccount("Mary Jane", "123456789", 1000)
```   
2. Deposit money into the account:
```
account.deposit(500)
```      
3. Withdraw money from the account:
```
account.withdraw(200)
```   
4. Check the account balance:
```
account.get_balance()
```   
# Example 2: Rectangle and Square classes   
This example demonstrates the creation of a `Rectangle` class that represents a rectangle object. The class includes attributes for the length and width of the rectangle, and methods for calculating the area and perimeter of the rectangle.   

A `Square` class is then created that inherits from `Rectangle`, and has a method for calculating the diagonal length of the square. The `Square` class also overrides the `set_length` and `set_width` methods of the parent class to ensure that the length and width of the square are always equal.   

## How to use the Rectangle and Square classes   
1. Create an instance of the `Rectangle` class by passing in the length and width:
```
rectangle = Rectangle(10, 5)
```   
2. Calculate the area of the rectangle:
```
rectangle.area()
```   
3. Calculate the perimeter of the rectangle:
```
rectangle.perimeter()
```   
4. Create an instance of the Square class by passing in the side length:
```
square = Square(5)
```
5. Calculate the area of the square:
```
square.area()
```
6. Calculate the perimeter of the square:
```
square.perimeter()
```
7. Calculate the diagonal length of the square:
```
square.diagonal()
```
