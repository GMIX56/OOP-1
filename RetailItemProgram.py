import RetailItemClass as r

i1 = r.RetailItem('Jacket',12,59.95)
i2 = r.RetailItem('Jeans',40,34.99)
i3 = r.RetailItem('Shirt',20,24.95)

print('Item 1:')
print(f'Description: {i1.description}')
print(f'Units: {i1.units}')
print(f'Price: {i1.price}\n')
      
print('Item 2:')
print(f'Description: {i2.description}')
print(f'Units: {i2.units}')
print(f'Price: {i2.price}\n')

print('Item 3:')
print(f'Description: {i3.description}')
print(f'Units: {i3.units}')
print(f'Price: {i3.price}')