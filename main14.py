def check_name():
    return input('Кто создатель Python?: ').upper()


while check_name() != "ГВИДО":
    print('Неправильно, подумай еще!')
    check_name()
print('Верно!')
