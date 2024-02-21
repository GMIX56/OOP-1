import InsectClass as i

mosquito = i.Insect()
housefly = i.Insect()


mosquito.calc_flight()
housefly.calc_flight()

print(f"the mosquito can fly up to {mosquito.get_miles()} miles")
print(f"the housefly can fly up to {housefly.get_miles()} miles")