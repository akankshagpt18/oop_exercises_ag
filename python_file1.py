# Question 1 and 2
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


vehicle1 = Vehicle("Tesla Model S", 250, 18)

print(vehicle1.name, vehicle1.max_speed, vehicle1.mileage)


# Question 4

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        avg = sum(self.marks)/len(self.marks)
        return avg

student1 = Student('Alice', [45,35,30,40])
print(student1.name, student1.average())

# Exercise 6

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        return self.balance + amount
    def withdraw(self, amount):
        if self.balance <amount:
            return "Insuffiecient balance"
        else:
            return self.balance - amount

acct = BankAccount(1000)
print(f"Balance is: {acct.balance} and deposited amount is {acct.deposit(10)}")
print(f"Balance is: {acct.balance} and withdrawn amount is {acct.withdraw(20)}")
print(f"Balance is: {acct.balance} and withdrawn amount is {acct.withdraw(1001)}")


