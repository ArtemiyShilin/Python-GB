birh_year = '1998'
print('Тип переменной age =', type(birh_year))

period = 23
print('Тип переменной period =', type(period))

#приведение к типу данных интеджер и вывод
age = int(birh_year) + period
print(age)

#приведение к типу данных стринг и вывод
stroka = birh_year + str(period)
print(stroka)