from random import random

number = int(random() * 100)
print(number)
value = int(input("Введите число от 1 до 100"))
if value == number:
    print('Вы угадали')
else:
    if value > number:
        print('меньше')
    else:
        print('больше')
