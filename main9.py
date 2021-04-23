flag=True
while flag:
    try:
        age = int(input('Сколько вам лет? '))
    except Exception:
        print('Это не число. Иди нахуй.')
        print('Введите целое число цифрами')
        flag = True if input('Начать заново?(Y/N)') == 'Y' else False
    else:
        period=20
        age_period = age + period
        print('Через', period, 'вам будет', age_period)
        flag = True if input('Начать заново?(Y/N)') == 'Y' else False

#age = int(input('Сколько вам лет? '))
##period = int(input('Укажите прериод '))
#age_period = age + period
#print('Через', period, 'вам будет', age_period)
