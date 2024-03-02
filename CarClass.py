'''
Write a class named RetailItem that holds data about an item in a retail store. 
The class should store the following data in attributes: item description, units 
in inventory, and price. Once you have written the class, write a program that 
creates three RetailItem objects and stores the following data in them:
'''

class Car:
    def __init__(self,year_model,make):
        self.__year_model=year_model
        self.__make=make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5
        if self.__speed < 0:
            self.__speed = 0
        
    def get_speed(self):
        return self.__speed