n = int(input("Введите число:"))

while 0 < n > 10:
    print("Число не верное")
    n = int(input("Введите число:"))

else:
    print("Возвожу в квадрат", n ** 2)