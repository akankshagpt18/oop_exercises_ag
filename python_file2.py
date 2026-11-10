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

        