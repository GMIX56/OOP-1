'''
 Write a class named Car that has the following data attributes:
    _ _year_model (for the car’s year model)
    _ _make (for the make of the car)
    _ _speed (for the car’s current speed)
The Car class should have an _ _init_ _ method that accepts the car’s 
year model and make as arguments. These values should be assigned to 
the object’s _ _year_model and _ _make data attributes. It should also 
assign 0 to the _ _speed data attribute.
The class should also have the following methods:
    accelerate - The accelerate method should add 5 to the speed data attribute each time it is called.
    brake - The brake method should subtract 5 from the speed data attribute each time it is called.
    get_speed - The get_speed method should return the current speed.
Next, design a program that creates a Car object then calls the accelerate method five times.
After each call to the accelerate method, get the current speed of the car and display it. 
Thencall the brake method five times. After each call to the brake method, get the current 
speed of the car and display it.
'''

import CarClass as c

car = c.Car(1932,'Scout Scarab')

print(f'\n{car._Car__year_model} {car._Car__make}\n')

print('Accelerating:')
for i in range(5):
    car.accelerate()
    print(f'Speed: {car.get_speed()}')
print()

print('Breaking:')
for i in range(5):
    car.brake()
    print(f'Speed: {car.get_speed()}')