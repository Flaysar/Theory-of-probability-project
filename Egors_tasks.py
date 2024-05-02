from random import randint
from random import uniform
import math
from functions import local_lapl
from functions import integr_lapl
from functions import transposition
from functions import transposition_with_repeat
from functions import combination
from functions import combination_with_repeat
from functions import placement
from functions import placement_with_repeat
from functions import discr_math_expectation
from functions import discr_dispersion
from functions import discr_standart_deviation


# 1-ое задание
def task_1():
    answer = '1. '
    n = randint(3, 4)
    text = f'1. На штрафной стоянке наугад выбирают автомобиль с номером из {n} цифр. Найти вероятность того, что его номер: \na) '
    rand_condition = randint(1, 3)  # пусть это разные условия для одной задачи
    if rand_condition == 1:
        my_rand = randint(1, 2)  # это разные формулировки одной задачи
        if my_rand == 1:
            text += 'не содержит четных цифр \n'
        else:
            text += 'все числа нечетны \n'
        answer += f'a) 5^{n} или {5 ** n}'

    elif rand_condition == 2:
        my_rand = randint(1, 2)
        if my_rand == 1:
            text += 'не содержит нечетных цифр \n'
        else:
            text += 'все числа четны\n'
        answer += f'a) 5^{n} или {5 ** n}'
    else:
        rand1 = randint(0, 9)
        rand2 = randint(0, 9)
        while (rand1 == rand2): rand2 = randint(0, 9)
        text += f'не содержит цифры {rand1} и {rand2} \n'  # с помощью f' {какая-то переменная}' можно вставлять переменные в строки
        answer += f'a) 8^{n} или {8 ** n}'

    type = randint(0, 1)
    if type == 0:
        text += f'б) Содержит цифру {randint(0, 9)}\n'
        text += answer + f', б) {n}*10^{n - 1} или {n * 10 ** (n - 1)}'
    else:
        rand1 = randint(0, 9)
        rand2 = randint(0, 9)
        while (rand1 == rand2): rand2 = randint(0, 9)
        place = randint(1, n)
        text += f'б) На {place}-ом месте содержит цифру {rand1} или {rand2}\n'
        answer += f', б) 2*10^{n - 1} или {2 * 10 ** (n - 1)}'
    return text, answer


def task_2():
    answer = '2. '
    love_songs = randint(13, 18)
    songs_need = love_songs - 3
    anim_songs = love_songs - 5
    text = f'2. Для очередной передачи «Угадай мелодию» было подготовлено {love_songs * 2} песен ' \
           f'из которых {love_songs} — о любви, {anim_songs} — о животных, остальные — о погоде. ' \
           f'В первом туре прозвучало {songs_need} песен. Найти вероятность того, что: \n'
    type = randint(0, 1)
    if type == 0:
        text += f'a) Все {songs_need} песен о любви.\n'
        answer += f'C({love_songs} по {songs_need})/C({love_songs * 2} по {songs_need}'
    else:
        text += f'a) Из {songs_need} песен нет ни одной о любви.\n'
        answer += f'C({love_songs} по {songs_need})/C({love_songs * 2} по {songs_need})'

    rand1 = randint(2, int(songs_need / 2) - 1)
    rand2 = songs_need - 2 - rand1
    text += f'б) не менее {rand2} песен о любви и не менее {rand1} песен о животных.\n'
    answer += f', б) ( C({love_songs} по {rand2}) * C({anim_songs} по {rand1}) * ' \
              f'C({love_songs * 2 - rand1 - rand2} по {songs_need - rand1 - rand2}) ) / C({love_songs * 2} по {songs_need})'
    return text, answer


def task_3():
    text = '3. По мишени производится три выстрела. Рассматриваются события: ' \
           'Ai — попадание при i"м выстреле (i = 1, 2, 3). В алгебре событий выразить следующие события: ' \
           'А — все три попадания; В — хотя бы один промах, С — не больше одного попадания, ' \
           'D — попадание в мишень не раньше, чем при третьем выстреле.'
    return text


def task_4():
    answer = '4. '
    rand1 = round(uniform(0.1, 0.7), 1)
    rand2 = round(uniform(0.1, 0.7), 1)
    while (rand1 == rand2): rand2 = round(uniform(0, 9), 1)
    text = f'4. Контролер заметила, что вероятность встретить в трамвае мэра города равна {rand1}, ' \
           f'а местную знаменитость — фокусника — {rand2}. Чему равна вероятность того, что завтра ' \
           'утром контролер проверит билет:\n'
    if randint(0, 1) == 0:
        text += 'a) у мэра;\n'
        answer += f'a) {rand1}'
    else:
        text += 'a) у фокусника;\n'
        answer += f'a) {rand2}'
    text += 'б) и у мэра, и у фокусника;\n'
    answer += f', б) {round(rand1 * rand2, 3)}'
    text += 'в) Хотя бы у одного;\n'
    answer += f', в) {round(rand1 * rand2 + rand1 * (1 - rand2) + rand2 * (1 - rand1), 3)}'
    return text, answer


def task_5():
    answer = '5. '
    rand1 = round(uniform(0.4, 0.7), 1)
    rand2 = round(uniform(0.1, min(0.4, 1 - rand1)), 1)
    concerts = randint(4, 5)
    termination = 'концертов'
    if concerts == 4: termination = 'концерта'
    city_list = ('Париже', 'Лондоне', 'Будапеште', 'Праге')
    rand_city = randint(0, 3)
    text = f'5. Знаменитая эстрадная певица с вероятностью {rand1} ' \
           f'дает концерты у себя на родине, с вероятностью {rand2} — в {city_list[rand_city]}. ' \
           f'Этой осенью она дала {concerts} {termination}. ' \
           f'Какова вероятность того, что концертов в {city_list[rand_city]} было больше?\n'
    sum = 0
    for i in range(int(concerts / 2) + 1, concerts + 1):
        sum += combination(concerts, i)[1] * (rand2 ** i) * (1 - rand2) ** (concerts - i)
    if (1 - rand2 - rand1) > 0:
        for i in range(1, int(concerts / 2) + 1):
            if i == 1:
                sum += combination(concerts, 1)[1] * (1 - rand1 - rand2) ** (concerts - 1) * rand2
            elif i == 2:
                sum += combination(concerts, 2)[1] * rand2 ** 2 * (1 - rand1 - rand2) ** (concerts - 2) + \
                       combination(concerts, 2)[1] * rand2 ** 2 * (1 - rand2 - rand1) ** (concerts - 3) * rand1 * \
                       combination(concerts - 2, 1)[1]
    sum = round(sum, 4)
    return text, answer


def task_6():
    type = randint(0, 2)
    task = ''
    answer = '6. '
    if type == 0:
        task = 'оба кубика зеленые'
    elif type == 1:
        task = 'оба кубика розовые'
    else:
        task = 'один кубик зеленый, другой - розовый'
    green = randint(5, 7)
    purple = randint(2, 4)
    text = f'6. В коробке находится {purple} розовых и {green} зеленых кубиков. Из коробки наугад достают два кубика. ' \
           f'Найти вероятность того, что {task} (извлеченный первый кубик обратно не положили).\n'
    if type == 0:
        answer += f'{green}/{green + purple} * {green - 1}/{green + purple - 1} или ' \
                  f'{round(green / (green + purple) * (green - 1) / (green + purple - 1), 4)} '
    elif type == 1:
        answer += f'{purple}/{green + purple} * {purple - 1}/{green + purple - 1} или ' \
                  f'{round(purple / (green + purple) * (purple - 1) / (green + purple - 1), 4)} '
    else:
        answer += f'{purple}/{green + purple} * {green}/{green + purple - 1} + ' \
                  f'{green}/{green + purple} * {purple}/{green + purple - 1} или ' \
                  f'{round((purple / (green + purple) * green / (green + purple - 1) * 2), 4)}'
    return text, answer


def task_7():
    answer = '7. '
    rand1 = randint(1, 3) * 10
    rand2 = randint(2, 4) * 10
    rand3 = (100 - rand1 - rand2)
    while (rand1 == rand2): rand2 = randint(2, 4) * 10
    chance1 = round(uniform(0.4, 0.6), 1)
    chance2 = round(uniform(0.5, 0.8), 1)
    while chance1 == chance2: chance2 = round(uniform(0.5, 0.8), 1)
    chance3 = round(uniform(0.8, 0.9), 1)
    if chance2 == 0.8: chance3 = 0.9
    formulation = 'одном случае'
    if chance3 == 0.8: formulation = 'двух случаях'
    text = f'7. Для защиты от грабителей {rand1}% квартир оборудованы пожарной сиреной, в {rand2}% квартир ' \
           'в дверях заложены пиропатроны, а в остальных квартирах содержатся гремучие змеи. Пожарная сирена ' \
           f'отпугивает грабителей с вероятностью {chance1}, взрыв пиропатрона — с вероятностью {chance2}, а ограбить ' \
           f'квартиру с гремучими змеями удается лишь в {formulation} из десяти. Найти вероятность того, что ' \
           'грабителям удастся сделать свое черное дело, если квартира выбирается наугад.\n'
    answer += f'{round(rand1 / 100 * (1 - chance1) + rand2 / 100 * (1 - chance2) + rand3 / 100 * (1 - chance3), 4)}'
    return text, answer


def task_8():
    rand1 = randint(2, 5)
    rand2 = randint(2, 5)
    while rand1 == rand2: rand2 = randint(2, 5)
    rand3 = randint(2, 5)
    while (rand1 == rand3) or (rand2 == rand3): rand3 = randint(2, 5)
    wind = ['флейта', 'фагот', 'валторна', 'дудка', 'саксофон']
    wind_str = ''
    for i in range(0, rand1):
        wind_str += wind[i] + ', '
    wind_str = wind_str[:-2]
    percussion = ['барабан', 'ксилофон', 'бубен', 'маракасы', 'джембе']
    percussion_str = ''
    for i in range(0, rand2):
        percussion_str += percussion[i] + ', '
    percussion_str = percussion_str[:-2]
    stringed = ['скрипка', 'гитара', 'балалайка', 'клевесин', 'мандолина']
    stringed_str = ''
    for i in range(0, rand3):
        stringed_str += stringed[i] + ', '
    stringed_str = stringed_str[:-2]
    chance1 = round(uniform(0.2, 0.4), 1)
    chance2 = round(uniform(0.4, 0.5), 1)
    while chance1 == chance2: chance2 = round(uniform(0.4, 0.5), 1)
    chance3 = round(uniform(0.6, 0.8), 1)
    rand_inst = randint(0, rand3 - 1)
    task = 'была'
    if rand_inst == 3: task = 'был'
    text = f'3. В студенческом оркестре {rand1} духовых инструмента ({wind_str}), {rand2} ударных ({percussion_str}) ' \
           f'и {rand3} струнных ({stringed_str}). В комнате, где хранятся музыкальные инструменты, сыро, и ' \
           f'вероятность того, что инструмент будет расстроен, для духовых инструментов равна {chance1}, для ' \
           f'ударных — {chance2}, для струнных — {chance3}. Перед концертом настройщик берет наугад инструмент, ' \
           f'который оказывается в хорошем состоянии. Найти вероятность того, что это {task} {stringed[rand_inst]}.\n'
    answer = '8. '
    sum = rand1 + rand2 + rand3
    chance_good = round(rand1 / sum * (1 - chance1) + rand2 / sum * (1 - chance2) + rand3 / sum * (1 - chance3), 4)
    answer += f' {round((1 - chance3) * 1 / sum / chance_good, 4)}'
    return text, answer


def task_9():
    chance = round(uniform(0.7, 0.9), 1)
    bad_chance = round(1 - chance, 1)
    num = randint(8, 10)
    type = f'будет, по меньшей мере, {num - 1} успешных'
    var = randint(0, 2)
    if var == 1:
        type = 'будет не более 1 провала'
    elif var == 2:
        type = f'все будут успешны'

    text = '9. Вероятность успешного запуска управляемого снаряда ' \
           f'равна {chance}. Найти вероятность того, что из {num} запусков ' \
           f'{type}.\n'
    answer = '9. '
    if var == 0 or var == 1:
        answer += f'{chance}^{num} + C({num} по {num - 1}) * {chance}^{num - 1} * {bad_chance} или ' \
                  f'{round(chance ** num + combination(num, num - 1)[1] * chance ** (num - 1) * bad_chance, 4)}'
    elif var == 2:
        answer += f'{chance}^{num} или {round(chance ** num, 4)}'
    return text, answer


def task_10():
    chance_list = [0.75, 0.8, 0.85, 0.9]
    chance = chance_list[randint(0, 3)]
    bad_chance = round(1 - chance, 2)
    num_list = [90, 100, 110]
    num = num_list[randint(0, 2)]
    exactly = num - list([20, 25, 30])[randint(0, 2)]
    text = f'10. Всхожесть семян составляет {round(chance * 100)}%. Найти вероятность того, ' \
           f'что из {num} семян взойдет: \nа) ровно {exactly}; ' \
           f'\nб) не менее {exactly} и не более {exactly + 15}.\n'
    answer = '10. '
    x = round((exactly - num * chance) / (num * chance * bad_chance), 2)
    y = round((exactly + 15 - num * chance) / (num * chance * bad_chance), 2)
    answer += f'a) {local_lapl(x)}, б) {round(integr_lapl(y) - integr_lapl(x), 4)}'
    return text, answer


def task_11():
    num = list([600, 700, 800, 900])[randint(0, 3)]
    chance = round(uniform(0.004, 0.01), 3)
    count = randint(8, 12)
    text = f'11. На прядильной фабрике работница обслуживает {num} веретен. ' \
           'При вращении веретена пряжа рвется в случайные моменты времени из-за ' \
           'неравномерности натяжения, неровности и других причин. Считая, что ' \
           'вероятность обрыва пряжи на каждом из веретен в течение времени Т ' \
           f'равна {chance}, найти вероятность того, что за это время произойдет {count} обрывов.\n'
    answer = '11. '
    lamb = round(num * chance)
    probability = lamb ** count / math.factorial(count) * math.exp(-lamb)
    answer = f'{lamb}^{count} / {count}! * e^-{lamb} или {round(probability, 4)}'
    return text, answer


def task_12():
    chance = round(uniform(0.2, 0.4), 1)
    bad_chance = 1 - chance
    count = randint(3, 5)
    text = '12. Вероятность того, что в библиотеке необходимая студенту книга свободна, ' \
           f'равна {chance}. Составить ряд распределения числа библиотек, которые посетит студент, ' \
           f'если в городе {count} библиотеки. Найти М(Х), D(X), (X), F(X) этой случайной величины. ' \
           'Построить график F(X).\n'
    answer = '12.\n '
    for i in range(1, count + 1):
        answer += f'{i}\t'
    answer += '\n'
    count_dict = {}
    in_first_bib = chance
    for i in range(1, count + 1):
        if i == count:
            in_first_bib /= chance
            count_dict[i] = round(in_first_bib, 3)
            answer += f'{count_dict[i]}\t'
        else:
            count_dict[i] = round(in_first_bib, 3)
            answer += f'{count_dict[i]}\t'
        in_first_bib *= bad_chance
    answer += '\n'
    Mx = discr_math_expectation(count_dict)
    Dx = discr_dispersion(count_dict)
    std = discr_standart_deviation(count_dict)
    answer += f'M(x) = {Mx}, D(x) = {Dx}, Отклонение = {std}'
    return text, answer


def task_13():
    chance = round(uniform(0.4, 0.8), 1)
    while (chance == 0.5): chance = round(uniform(0.4, 0.8), 1)
    bad_chance = 1 - chance
    count = randint(2, 4)
    text = f'13. Производится стрельба по цели. Вероятность попадания при каждом выстреле равна {chance}. ' \
           f'Составить ряд распределения случайной величины Х — числа попаданий по цели при {count} выстрелах. ' \
           'Найти M(X) и D(X) этой случайной величины.\n'
    answer = '13. \n'
    for i in range(0, count + 1):
        answer += f'{i}\t'
    answer += '\n'
    count_dict = {}
    for i in range(0, count + 1):
        count_dict[i] = round(combination(count, i)[1] * chance ** i * bad_chance ** (count - i), 4)
        answer += f'{count_dict[i]}\t'
    answer += '\n'
    Mx = discr_math_expectation(count_dict)
    Dx = discr_dispersion(count_dict)
    answer += f'M(X) = {Mx}, D(X) = {Dx}'
    return text, answer


def task_14():
    count_list = [500, 1000, 2000, 4000]
    lamb_list = [1, 2, 4]
    rand_count = randint(0, 3)
    rand_lamb = randint(0, 2)
    count = count_list[rand_count]
    lamb = lamb_list[rand_lamb]
    chance = round(lamb / count, 5)
    text = f'14. Радиоаппаратура состоит из {count} электроэлементов. Вероятность отказа ' \
           f'одного элемента в течение года работы равна {chance} и не зависит от состояния других ' \
           'элементов. Составить ряд распределения числа элементов, которые выйдут из строя в ' \
           'течение года работы радиоаппаратуры. Найти M(X) этой случайной величины.\n'
    print(text)
    answer = '14.\n'
    for i in range(0, 3):
        answer += f'{i}\t'
    answer += '...\t'
    answer += 'k\t\t...\n'
    answer += f'{round(math.exp(-lamb), 3)}\t'
    for i in range(1, 3):
        answer += f'{round(lamb ** i / math.factorial(i) * math.exp(-lamb), 3)}\t'
    answer += '\tλ^k/k!*e^(-λ)\t...\n'
    answer += f'M(X) = n * p = {lamb}'
    return text, answer


def task_15():
    text = 'Независимые случайные величины X и Y заданы таблицами распределений. \n' \
           'Найти:\n1) M(X), M(Y), D(X), D(Y);\n2) таблицы распределения случайных величин Z1 = ' \
           '2X+Y, Z2 = X*Y; \n3) M(Z1), M(Z2), D(Z1), D(Z2) непосредственно по таблицам распределений ' \
           'и на основании свойств математического ожидания и дисперсии.\n'
    rand1 = randint(-6, -3)
    rand2 = randint(-1, 1)
    rand3 = randint(3, 8)
    text += f'X:\t{rand1}\t{rand2}\t{rand3}\n'
    chance1 = round(uniform(0.1, 0.8), 1)
    chance2 = round(uniform(0.1, 0.9 - chance1), 1)
    chance3 = round(1 - chance1 - chance2, 1)
    x_dict = {}
    place = randint(1, 3)
    if place == 1:
        text += f'P:\tp\t{chance1}\t{chance2}\n'
        x_dict[rand1] = chance3
        x_dict[rand2] = chance1
        x_dict[rand3] = chance2
    elif place == 2:
        text += f'P:\t{chance1}\tp\t{chance2}\n'
        x_dict[rand1] = chance1
        x_dict[rand2] = chance3
        x_dict[rand3] = chance2
    else:
        text += f'P:\t{chance1}\t{chance2}\tp\n'
        x_dict[rand1] = chance1
        x_dict[rand2] = chance2
        x_dict[rand3] = chance3

    y_dict = {}
    y1 = randint(-7, 7)
    while (y1 == 0): y1 = randint(-7, 7)
    y2 = randint(-7, 7)
    while (y1 == y2 or y2 == 0): y2 = randint(-7, 7)
    y_chance1 = round(uniform(0.1, 0.8), 1)
    y_chance2 = round(1 - y_chance1, 1)
    y_dict[y1] = y_chance1
    y_dict[y2] = y_chance2
    text += f'\nY:\t{y1}\t{y2}\n'
    text += f'P:\t{y_chance1}\t{y_chance2}\n'

    MX = discr_math_expectation(x_dict)
    DX = discr_dispersion(x_dict)
    MY = discr_math_expectation(y_dict)
    DY = discr_dispersion(y_dict)

    answer = '15.\n'
    answer += f'M(X) = {MX}, D(X) = {DX}, M(Y) = {MY}, D(Y) = {DY}\n'
    Z1_dict = {}
    for x, px in x_dict.items():
        for y, py in y_dict.items():
            Z1_dict[2 * x + y] = round(px * py, 3)
    answer += 'Z1:\t'
    for i in Z1_dict.keys():
        answer += f'{i}\t'
    answer += '\nP:\t'
    for val in Z1_dict.values():
        answer += f'{val}\t'
    MZ1 = discr_math_expectation(Z1_dict)
    DZ1 = discr_dispersion(Z1_dict)
    answer += f'\nM(Z1) = {MZ1}, D(Z1) = {DZ1}\n\n'

    Z2_dict = {}
    for x, px in x_dict.items():
        for y, py in y_dict.items():
            Z2_dict[x * y] = round(px * py, 3)
    answer += 'Z2:\t'
    for i in Z2_dict.keys():
        answer += f'{i}\t'
    answer += '\nP:\t'
    for val in Z2_dict.values():
        answer += f'{val}\t'
    MZ2 = discr_math_expectation(Z2_dict)
    DZ2 = discr_dispersion(Z2_dict)
    answer += f'\nM(Z2) = {MZ2}, D(Z2) = {DZ2}'

    return text, answer


def task_16():
    answer = '16.\n '
    type = randint(1, 2)
    if type == 1:
        text = '16. Дана функция распределения F(x) непрерывной случайной величины X.\n' \
               'Требуется:\n1) найти плотность вероятности f(x);\n2) построить графики F(x) и f(x);\n' \
               '3) найти M(X), D(X), (Х);\n4) найти Р(α < X < β) для данных α, β\n'
        text += '\t |\t0, x <= π/6;\nF(x)=|\t-cos3x, π/6 < x <= π/3;\n\t |\t1, x > π/3;\n'

        alfa = 'π/6'
        beta = 'π/4'
        alfa_type = randint(1, 2)
        if alfa_type == 2:
            alfa = 'π/4'
            beta = 'π/3'
        text += f'α = {alfa}, β = {beta}\n'

        answer += '\t |\t0, x <= π/6;\nf(x)=|\t3sin3x, π/6 < x <= π/3;\n\t |\t0, x > π/3;\n'
        answer += 'M(X) = (π-1)/3, M(X^2) = (π^2-π-2)/9, \nD(X) = (π^2-π-2)/9 - (π-1)/3 = (π^2-4π+1)/9, ' \
                  'Отклонение = √(π^2-4π+1)/3\n'
        if alfa_type == 1:
            answer += f'P(α < x < β) = P({alfa} < x < {beta}) = √2/2'
        else:
            answer += f'P(α < x < β) = P({alfa} < x < {beta}) = 1 - √2/2'
    else:
        text = '16. Дана функция распределения F(x) непрерывной случайной величины X.\n' \
               'Требуется:\n1) найти плотность вероятности f(x);\n2) построить графики F(x) и f(x);\n' \
               '3) найти M(X), D(X), (Х);\n4) найти Р(α < X < β) для данных α, β\n'
        text += '\t |\t0, x <= 7π/6;\nF(x)=|\tcos3x, 7π/6 < x <= 4π/3;\n\t |\t1, x > 4π/3;\n'

        alfa = '7π/6'
        beta = '5π/4'
        alfa_type = randint(1, 2)
        if alfa_type == 2:
            alfa = '5π/4'
            beta = '4π/3'
        text += f'α = {alfa}, β = {beta}\n'

        answer += '\t |\t0, x <= 7π/6;\nf(x)=|\t-3sin3x, 7π/6 < x <= 4π/3;\n\t |\t0, x > 4π/3;\n'
        answer += 'M(X) = (4π-1)/3, M(X^2) = (16π^2-7π-2)/9, \nD(X) = (16π^2-7π-2)/9 - (4π-1)/3 = (16π^2-19π+1)/9, ' \
                  'Отклонение = √(16π^2-19π+1)/3\n'
        if alfa_type == 1:
            answer += f'P(α < x < β) = P({alfa} < x < {beta}) = √2/2'
        else:
            answer += f'P(α < x < β) = P({alfa} < x < {beta}) = 1 - √2/2'

    return text, answer


def task_17(): # !!!!!!!!!!!!!!!!!!!!
    answer = '17.\n '

    text = '17. Дана функция распределения f(x) непрерывной случайной величины X.\n' \
           'Требуется:\n1) найти параметр a;\n2) Найти функцию распределния F(x);\n' \
           '3) построить графики f(x) и F(x);\n4) найти ассиметрию и эксцесс\n'
    text += '\t |\t0, x <= 0;\nf(x)=|\taxe^(-x^2), x > 0;\n'

    answer += 'a = 2\n\t |\t0, x <= 0;\nF(x)=|\te^(-x^2)+1, x > 0;\n'


    return text, answer

def task_18():
    answer = '18.\n '
    alfa = randint(-3, 0)
    beta = randint(1, 3)
    text = '18. 1) проверить свойство  ∫( f(x)dx ) = 1;\n'\
        '2) построить график f(x);\n3) найти функцию распределения F(x);\n'\
        '4) найти Р(α < X < β) для данных α, β;\n5) найти М(Х), D(X), σ(X).\n'
    text += '\t |\t0, x <= -1;\n\t |\t1/4 * (x+1), -1 < x <= 1;\nf(x)=|\t1/4 * (3-x), 1 < x <= 3;\n\t |\t0, x>3;\n'
    text += f'α = {alfa}, β = {beta}\n'

    answer += '\t |\t0, x <= -1;\n\t |\t1/4 * (x^2/2 + x), -1 < x <= 1;\nF(x)=|'\
    '\t1/4 * (3x - x^2/2), 1 < x <= 3;\n\t |\t1, x>3;\n'
    num = round(1/4 * (3*beta - beta**2/2) - 1/4 * (3 - 1/2), 3)
    if alfa!=0:
        num+= round(1/4 * (1/2 + 1) - 1/4 * (1/2 - 1), 3)
    else:
        num+= round(1/4 * (1/2 + 1), 3)
    answer += f'Р(α < X < β) = P({alfa} < X < {beta}) = {num}\n'

    MX = round(1/4 * (1**3/3 + 1**2/2) - 1/4 * (-1**3/3 + -1**2/2), 3)
    MX += round(1/4 * (3*3**2/2 - 3**3/3) - 1/4 * (3*1**2/2 - 1**3/3), 3)
    MX2 = round(1 / 4 * (1 ** 4 / 4 + 1 ** 3 / 3) - 1 / 4 * (-1 ** 4 / 34+ -1 ** 3 / 3), 3)
    MX2 += round(1 / 4 * (3 * 3 ** 3 / 3 - 3 ** 4 / 4) - 1 / 4 * (3 * 1 ** 3 / 3 - 1 ** 4 / 4), 3)
    DX = round(MX2 - MX**2, 3)
    std = round(math.sqrt((DX)), 3)
    answer+=f'M(X) = {MX}, D(X) = {DX}, Отклонение = {std}'

    return text, answer

t, a = task_18()
print(t, a)
