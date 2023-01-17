""" Name : Mosammat Muna Project : Python Final Capstone Project
    Objective: Program create two classes Employee and ProductionWorker.Employee class contains basic information of an
    employee and ProductionWorker class inherit the Employee class and contains additional information related to
    employee's shift and pay rate. Also, taking input from user and displaying the entered information."""

import datetime
import os

class Employee:
    # Constructor to initialize attributes
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    # -------- Setters sets attributes--------
    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    # -------- Getters returns units attribute----
    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

class ProductionWorker(Employee):
    """ constructor for ProductionWorker subclass,accepts name, number, shift, pay_rate as
       arguments and calls the constructor of superclass Employee to initialize name and number """
    def __init__(self, name, number, shift, pay_rate):
        Employee.__init__(self, name, number)
        self.__shift = shift
        self.__pay_rate = pay_rate

    # -------- Setters sets attributes--------
    def set_shift(self, shift):
        self.__shift = shift

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    # -------- Getters returns units attribute----
    def get_shift(self):
        return self.__shift

    def get_pay_rate(self):
        return self.__pay_rate

def main():
    userpath = os.environ.get('path')
    print(userpath[:38])  # Display working directory.

    os.environ['user'] = 'Programmer: Mosammat Muna'
    print(os.environ.get('user'))  # Display user profile.

    x = datetime.datetime.now()
    y = x.strftime("Lab 19.2 " + "%B %d,%Y" " @ " "%I:%M:%S")
    print(f"{y}\n")  # Display lab name,date and time.

    # Get user input with input validation
    while True:
        try:
            name = input("Enter your name: ")
            if not name.isalpha():
                raise ValueError("Error: Name must contain only alphabets.")
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            employeeName = input("Enter the employee's name: ")
            if not employeeName.isalpha():
                raise ValueError("Error: Employee name must contain only alphabets.")
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            number = int(input("Enter the ID number: "))
            if number < 0:
                raise ValueError("Error: ID number must be a positive integer.")
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            shift = int(input("Enter the shift number(1 for day shift or 2 for night shift): "))
            if shift not in [1, 2]:
                raise ValueError("Error: Shift must be either 1 or 2.")
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            pay_rate = float(input("Enter the hourly pay rate: "))
            if pay_rate < 0:
                raise ValueError("Error: Pay rate must be a positive number.")
            break
        except ValueError as e:
            print(e)

    worker = ProductionWorker(employeeName, number, shift, pay_rate)    # Create  objects from the ProductionWorker

    # Display information to the user
    print(f"{name}, here is the production worker, {employeeName}'s information:\n")
    print("Name:", worker.get_name())
    print("ID number:", worker.get_number())
    print("Shift:", worker.get_shift())
    print("Hourly pay rate: ${:.2f}".format(worker.get_pay_rate()))

main()
