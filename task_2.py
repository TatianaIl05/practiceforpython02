countries = []
coun = input('Введите названия стран: ').split()
for i in range(0, len(coun)-1, 2):
    countries. append(coun[i] + ' ' + coun[i+1])
print(countries)
