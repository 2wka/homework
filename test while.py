while True:
    number = int(input('Введиде число: '))
    if number % 2 == 0:
        print('Четное число!')
    else:
        print('Нечетное число!')
    answer = input('Вы довольны? ').upper()
    if answer == 'ДА':
        break
