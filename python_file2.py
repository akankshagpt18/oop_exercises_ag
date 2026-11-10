# Question 10
class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        return self.notes.append(note)

    def show_note(self):
        for i, note in enumerate(self.notes, start=1):
           print(f"{i}.{note}") 

nb= Notebook()
nb.add_note("Buy groceries")
nb.add_note("Read a book")
nb.add_note("Call the doctor")
nb.show_note()


# Exercise 11
class CoffeeMachine:
    def __init__(self, water, coffee, milk):
        self.water = water
        self.coffee = coffee
        self.milk= milk

    def make_latte(self):
        need_wtr= 200
        need_mlk= 150
        need_coffee = 20
        if self.water>need_wtr and self.milk> need_mlk and self.coffee>= need_coffee:
            self.water -= need_wtr
            self.milk -= need_mlk
            self.coffee -=need_coffee
            print(f"Latte made! Remaining - Water:{self.water}ml, Milk:{self.milk}ml and coffee:{self.coffee}mg")
        else: 
            print("Not enough resources to make a latte.")

coffee = CoffeeMachine(water=300, milk=200, coffee=30)
coffee.make_latte()
coffee.make_latte()




#Exercise 13

class Vehicle:
    def __init__(self, name, max_speed):
        self.name= name
        self.max_speed = max_speed

    def display(self):
        print(f"Vehiclename: {self.name} with the speed {self.max_speed}")

class Bus(Vehicle):
    pass

bus1 = Bus('School Bus', 40)
bus1.display()


# Exercise 15: Inheritance-super
class Vehicle:
    def __init__(self, base_fare):
        self.base_fare= base_fare

class Taxi(Vehicle):
    def __init__(self, base_fare):
        super().__init__(base_fare)
        self.maintenance_fee= base_fare *.10

    def total_fare(self):
        return self.base_fare + self.maintenance_fee

taxi = Taxi(20)
print(taxi.total_fare())

## Exercise 16: Polymorphism
class Animal:
    def speak(self):
        print('Animal says')

class Dog(Animal):
    def speak(self):
        print('Dogs says woof')
class Cat(Animal):
    def speak(self):
        print('Cat says meow')

dog = Dog()
cat = Cat()

dog.speak()
cat.speak()

# Exercise 17
class Employee:
    def __init__(self, name):
        self.name= name

    def calculate_pay(self):
        pass

class FullTimeEmployee(Employee):
    annual_salary = 12000


    def calculate_pay(self):
        return(f"Monthly salary will be: {self.annual_salary/12}")
    
class PartTimeEmployee(Employee):
    hours = 30
    hourly_rate= 50

    def calculate_pay(self):
        return(f"Monthly salary will be: {self.hours*self.hourly_rate*4}")

FTE = FullTimeEmployee("John")
PTE = PartTimeEmployee('Rob')

print(FTE.calculate_pay())
print(PTE.calculate_pay())
    