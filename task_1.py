from math import floor
total_cost = float(input('введите общую стоимость часов: '))
print(floor((total_cost-48*96)/(96/16)))