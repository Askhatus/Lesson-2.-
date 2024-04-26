while True:
    lenin = int(input('Год рождения В.И. Ленина: ')) # год рождения В.И.Ленина -1870 год.
    lennon = int(input('Год рождения Джона Леннона: ')) # год рождения Джона Леннона -1940 год.
    putin = int(input('Год рождения В.В. Путина: ')) # год рождения В.В.Путина -1952 год.
    petr_1 = int(input('Год рождения царя Петра 1-го: ')) # год рождения царя Петра 1-го -1672 год.
    ilon_mask = int(input('Год рождения Илона Маска: ')) # год рождения Илона Маска - 1971 год.
    gert = [lenin, lennon, putin, petr_1, ilon_mask]
    if lenin == 1870:
        lenin = True
    elif lenin != 1870:
        lenin = False
    if lennon == 1940:
        lennon = True
    elif lennon != 1940:
        lennon = False
    if putin == 1952:
        putin = True
    elif putin != 1952:
        putin = False
    if petr_1 == 1672:
        petr_1 = True
    elif petr_1 != 1672:
        petr_1 = False
    if ilon_mask == 1971:
        ilon_mask = True
    else:
        ilon_mask = False
    gert = [lenin, lennon, putin, petr_1, ilon_mask]
    answer_yes = []
    answer_no = []
    for i in gert:
        if i == True:
            answer_yes.append(i)
        if i == False:
            answer_no.append(i)
    print('Количество правильных ответов: -', len(answer_yes))
    print('Количество не правильных ответов: -', len(answer_no))
    print('Процент правильных ответов: -', (len(answer_yes)*100)/5, '%')
    print('Процент неправильных ответов: -', (len(answer_no)*100)/5, '%')
    games = input('Хотите продолжить игру? -')
    if games == 'Yes' or games == 'Да':
        True
    elif games == 'No' or games == 'Нет':
        break

