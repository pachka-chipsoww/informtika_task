import math

new_react = input('Название нового реактива:')
quantity = input('Количество:')
quantity = quantity.replace(',', '.')
quantity = math.floor(float(quantity))
print(f'Реактив {new_react} поступил на склад в количестве {quantity} шт.')
