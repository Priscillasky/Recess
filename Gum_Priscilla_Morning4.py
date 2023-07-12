#Day4 classes
#Example car

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def start_engine(self):
        print("Engine started")
    
    def stop_engine(self):
        print("Engine stopped")


my_car = Car("Toyota","Corolla",2022)
print(my_car.make)
print(my_car.model)
print(my_car.year)
my_car.start_engine()
my_car.stop_engine()

#Example 2
"""class Rectangle(15, 5):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)"""
    
    
#Example 3
class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} to account {self.account_number}")

    def withdraw(self, amount):
        if self.balance >=amount:
            self.balance -= amount

        else:
            print("Insufficient funds")

    def display_balance(self):
        print("Account Number:",self.account_number)
        print("Balance:",self.balance)

#Create a bank account object
my_account = BankAccount("123456789",1000)

#Perform operations on the bank account
my_account.display_balance()
my_account.deposit(500)
my_account.withdraw(200)
my_account.display_balance()

#Example 3 student
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:" ,self.age)

#create new student    
my_student = Student("Gum Priscilla",20)

#Display student details
my_student.display_info()



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print("Hello, my name is", self.name)
        print("I am", self.age, "years old")

#create a person object
my_person1 = Person("Gum Priscilla",20)
my_person2 = Person("Peninnah", 25)

print(my_person1.name)
print(my_person1.age)
print(my_person2.name)
print(my_person2.age)

#invoke method
my_person1.greet()
my_person2.greet()


#Exercise one
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    
    def circumference(self):
        return 2 * 3.14 * self.radius
    
    def display_info(self):
        print("Radius:", self.radius)
        print("Area:", self.area())
        print("Circumference:", self.circumference())

# circle object
my_circle = Circle(5)
print(my_circle.radius)
print(my_circle.area())
print(my_circle.circumference())
my_circle.display_info()  


#Exercise 2
#area and perimeter of a rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def display_info(self):
        print("Width:", self.width)
        print("Height:", self.height)
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())

# rectangle object
Rectangle = Rectangle(2,5)
print(Rectangle.width)
print(Rectangle.height)
print(Rectangle.area())
print(Rectangle.perimeter())

Rectangle.display_info()


#Exercise 3
#Calculate and display employee bonusses(15%) of salary (employee1:150000,employee2:230000)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        bonus = self.salary * 0.15
        return bonus

    def display_employee_details(self):
        bonus = self.calculate_bonus()
        total_salary = self.salary + bonus
        print(f"Employee: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Bonus: {bonus}")
        print(f"Total Salary: {total_salary}")
        print()

# Create Employee objects
employee1 = Employee("Gum", 150000)
employee2 = Employee("Priscilla", 230000)

# Display employee information
employee1.display_employee_details()
employee2.display_employee_details()

#Encapsulation
#main goals of encapsulation
"""
1. hide implementation of details of an object
2.protect object from changes
3.protect objects from external changes
4.code organisation and modularity

"""

#Example with bank accout
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number #encapsulates the account number
        self.balance = balance #encapsulates the balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} to account {self.account_number}")

    def withdraw(self, amount):
        if self.balance >=amount:
            self.balance -= amount

        else:
            print("Insufficient funds")

    def display_balance(self):
        return self.balance
    
    
my_account = BankAccount("364653622",10000)
    
print(my_account.account_number)
print(my_account.balance)
my_account.deposit(500)

print(my_account.balance)
print(my_account.withdraw)

#Exercise 2
#convert temperature from celcius (37 degrees celcius)to fahrenheit using encapslation

"""class tempConvert:
    def __init__(self, celcius):
        self._celcius = celcius


    def celcius_to_fahrenheit(self):
        return (self._celcius * 9/5) + 32
    
    def fahrenheit_to_celcius(self):
        return (self._fahrenheit - 32) * 5/9
    
#create object
my_fahrenheit = tempConvert(37)

print(my_fahrenheit.celcius_to_fahrenheit())
print(my_fahrenheit.fahrenheit_to_celcius())"""

#Solution


class TemperatureConverter:
    def __init__(self, celsius):
        self._celsius = celsius
        self._fahrenheit = None
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        self._celsius = value
        self._fahrenheit = None
    
    @property
    def fahrenheit(self):
        if self._fahrenheit is None:
            self._fahrenheit = (self._celsius * 9/5) + 32
        return self._fahrenheit

# Create an instance of the TemperatureConverter class
converter = TemperatureConverter(37)

# Access the Celsius temperature
print(f"Celsius: {converter.celsius}")

# Access the Fahrenheit temperature
print(f"Fahrenheit: {converter.fahrenheit}")

converter.celsius = 25

print(f"Celsius: {converter.celsius}")

print(f"Fahrenheit: {converter.fahrenheit}")

#Assignment 2: show  encapsulation with  employee information to give a  pay incrementation (Salary with emplyee information to new salary) e.g from 8500000 to 1000000




class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
    
    @property
    def name(self):
        return self._name
    
    @property
    def salary(self):
        return self._salary
    
    def give_pay_increment(self, increment_amount):
        self._salary += increment_amount

# Create an instance of the Employee class
employee = Employee("John Doe", 8500000)

# Display the initial employee information
print(f"Employee Name: {employee.name}")
print(f"Salary: {employee.salary}")

# Give a pay increment of 1500000
employee.give_pay_increment(1500000)

# Display the updated employee information
print(f"\nEmployee Name: {employee.name}")
print(f"Updated Salary: {employee.salary}")




