as_pushkin = int(input('Введите год рождения А.С.Пушкина: '))
if as_pushkin == 1799:
    den = input('Введите день рождения А.С.Пушкина: ')
    if den == '6 июня':
        print('Верно')
    else:
        print('Не верный день рождения.')
else:
    print('Неверный год')