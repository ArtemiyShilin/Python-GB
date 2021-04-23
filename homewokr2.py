while True:
    n = int(input("Введите число:"))
    if (0 < n and n < 10):
        print("Возвожу в квадрат", n ** 2)
        break
    else:
        print('Число не верное')
