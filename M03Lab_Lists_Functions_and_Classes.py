# M03 Lab - Case Study: Lists, Functions, and Classes
# Charles W
# Will take in attributes of a vehicle built
# on the back of a class and output data

class Vehicle:
    def __init__(self, vtype):
        self.vtype = vtype

class automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__(vtype)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


vtype = input('Vehicle type: ')
year = input('Input year: ')
make = input('Input make: ')
model = input('Input model: ')
doors = input('Input # of doors (2 or 4): ')
roof = input('Solid or Sun roof: ')
print()

v = automobile(year, make, model, doors, roof)

print("---------------------")
print('\nVehicle Type: ' + vtype)
print('\nYear: ' + v.year)
print('\nMake: ' + v.make)
print('\nModel: ' + v.model)
print('\n# of doors: ' + v.doors)
print('\nRoof type: ' + v.roof)