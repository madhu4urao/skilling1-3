#Banking system using oop
#parent class: User
#Holds details about user
#Has a function to show_user_details
#Child class:Bank
#stores details about the account balance
#stores details about the amount
#allows for deposits, withdraw and view balance

class User():
    def __init__(self, name, age, gender, phn_no):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone_number = phn_no
    def show_details(self):
        print("personal details")
        print(" ")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender :", self.gender)
        print("Phone Number: ", self.phone_number)

# Creating the child class
class Bank(User):
    def __init__(self, name, age, gender, phn_no):
        super().__init__(name, age, gender, phn_no)
        self.balance = 0

    def deposit(self, amount):
        self. amount = amount
        self.balance = self.balance + amount
        print("account balance has been updated : Rs", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("insufficient balance: Rs", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("successfully withdrawn and updated balance is: Rs", self.balance)

    def view_balance(self):
        self.show_details()
        print("updated balance is: Rs", self.balance)

anil = Bank("anil", 26, 'Male', 9999999)
anil.deposit(10000)
anil.withdraw(5000)
anil.view_balance()