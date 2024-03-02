pounds, inches = map(float, input('Введите вес (в фунтах) и рост (в дюймах): ').split())
kgs = pounds*0.45359237
cms = inches*2.54
print('ИМТ = ', round(kgs/(cms/100)**2, 2))
