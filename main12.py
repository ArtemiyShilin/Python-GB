age = int(input("Сколько вам лет?"))
if age < 18:
    print("Доступ запрещен")
elif age == 18:
    print("И что теперь делать?")
elif age > 18 and age <25:
    print('Вы счастливчик')
else:
    print('Доступ разрешен')
    if age%5 ==0:
        print('у вас юбилей ухухухх')
print('end')