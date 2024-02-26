import InsectClass as i

mosquito = i.Insect(2,4,'Mosquito')
housefly = i.Insect(2,4,'Housefly')


mosquito.calc_flight()
housefly.calc_flight()

print(f"the {mosquito.get_name()} can fly up to {mosquito.get_miles()} miles")
print(f"the {housefly.get_name()} can fly up to {housefly.get_miles()} miles")