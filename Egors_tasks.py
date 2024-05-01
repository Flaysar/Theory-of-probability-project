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


# 1-ое задание
def task_1():
    answer = ''
    n = randint(3, 4)
    text = f'1. На штрафной стоянке наугад выбирают автомобиль с номером из {n} цифр. Найти вероятность того, что его номер: \na) '
    rand_condition = randint(1, 3)  # пусть это разные условия для одной задачи
    if rand_condition == 1:
        my_rand = randint(1, 2)  # это разные формулировки одной задачи
        if my_rand == 1:
            text += 'не содержит четных цифр \n'
        else:
            text += 'все числа нечетны \n'
        answer += f'Ответ: a) 5^{n} или {5 ** n}'

    elif rand_condition == 2:
        my_rand = randint(1, 2)
        if my_rand == 1:
            text += 'не содержит нечетных цифр \n'
        else:
            text += 'все числа четны\n'
        answer += f'Ответ: a) 5^{n} или {5 ** n}'
    else:
        rand1 = randint(0, 9)
        rand2 = randint(0, 9)
        while (rand1 == rand2): rand2 = randint(0, 9)
        text += f'не содержит цифры {rand1} и {rand2} \n'  # с помощью f' {какая-то переменная}' можно вставлять переменные в строки
        answer += f'Ответ: a) 8^{n} или {8 ** n}'

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
        text += answer + f', б) 2*10^{n - 1} или {2 * 10 ** (n - 1)}'
    return text


def task_2():
    answer = ''
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
    text += answer + f', б) ( C({love_songs} по {rand2}) * C({anim_songs} по {rand1}) * ' \
                     f'C({love_songs * 2 - rand1 - rand2} по {songs_need - rand1 - rand2}) ) / C({love_songs * 2} по {songs_need})'
    return text


def task_3():
    text = '3. По мишени производится три выстрела. Рассматриваются события: ' \
           'Ai — попадание при i"м выстреле (i = 1, 2, 3). В алгебре событий выразить следующие события: ' \
           'А — все три попадания; В — хотя бы один промах, С — не больше одного попадания, ' \
           'D — попадание в мишень не раньше, чем при третьем выстреле.'
    return text


def task_4():
    answer = ''
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
    text += 'Ответ: ' + answer + f', в) {round(rand1 * rand2 + rand1 * (1 - rand2) + rand2 * (1 - rand1), 3)}'
    return text


def task_5():
    answer = ''
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
    text += f'Ответ: {sum}'
    return text


def task_6():
    type = randint(0, 2)
    task = ''
    answer = ''
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
    text += f'Ответ: {answer}'
    return text


def task_7():
    answer = ''
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
    text += "Ответ: " + answer
    return text


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
    answer = ''
    sum = rand1 + rand2 + rand3
    chance_good = round(rand1 / sum * (1-chance1) + rand2 / sum * (1-chance2) + rand3 / sum * (1-chance3), 4)
    answer += f'Ответ: {round((1-chance3) * 1 / sum / chance_good, 4)}'
    text += answer
    return text

def task_9():
    chance = round(uniform(0.7, 0.9), 1)
    bad_chance = round(1 - chance, 1)
    num =randint(8, 10)
    type = f'будет, по меньшей мере, {num-1} успешных'
    var = randint(0, 2)
    if var == 1:
        type = 'будет не более 1 провала'
    elif var ==2:
        type = f'все будут успешны'

    text = '9. Вероятность успешного запуска управляемого снаряда '\
    f'равна {chance}. Найти вероятность того, что из {num} запусков '\
    f'{type}.\n'
    answer = ''
    if var == 0 or var==1:
        answer += f'{chance}^{num} + C({num} по {num-1}) * {chance}^{num-1} * {bad_chance} или '\
        f'{round(chance**num + combination(num, num-1)[1] * chance**(num-1) * bad_chance, 4)}'
    elif var == 2:
        answer += f'{chance}^{num} или {round(chance**num, 4)}'
    text+=answer
    return text

def task_10():
    chance_list = [0.75, 0.8, 0.85, 0.9]
    chance = chance_list[randint(0, 3)]
    bad_chance = round(1 - chance, 2)
    num_list = [90, 100, 110]
    num = num_list[randint(0, 2)]
    exactly = num - list([20, 25, 30])[randint(0, 2)]
    text = f'10. Всхожесть семян составляет {round(chance*100)}%. Найти вероятность того, '\
    f'что из {num} семян взойдет: \nа) ровно {exactly}; '
    f'\nб) не менее {exactly} и не более {exactly+15}.\n'
    return text
     
def task_11():
    num = list([600, 700,  800, 900])[randint(0, 3)]
    chance = round(uniform(0.004, 0.01), 3)
    count = randint(8, 12)
    text = f'11. На прядильной фабрике работница обслуживает {num} веретен. '\
    'При вращении веретена пряжа рвется в случайные моменты времени из-за '\
    'неравномерности натяжения, неровности и других причин. Считая, что '\
    'вероятность обрыва пряжи на каждом из веретен в течение времени Т '\
    f'равна {chance}, найти вероятность того, что за это время произойдет {count} обрывов.\n'
    answer = ''
    lamb = round(num*chance)
    probability = lamb**count / math.factorial(count) * math.exp(-lamb)
    answer = f'{lamb}^{count} / {count}! * e^-{lamb} или {round(probability, 4)}'
    text+=answer
    return text


def task_12():
    chance = round(uniform(0.2, 0.4), 1)
    bad_chance = 1 - chance
    count = randint(3, 5)
    text = '12. Вероятность того, что в библиотеке необходимая студенту книга свободна, '\
    f'равна {chance}. Составить ряд распределения числа библиотек, которые посетит студент, '\
    f'если в городе {count} библиотеки. Найти М(Х), D(X), (X), F(X) этой случайной величины. '\
    'Построить график F(X).\n'
    answer = ''
    count_dict = {}
    in_first_bib = chance
    for i in range(1, count+1):
        if i==count:
            in_first_bib/= chance
            count_dict[i]=round(in_first_bib, 3)
        else:
            count_dict[i]=round(in_first_bib, 3)
        in_first_bib*=bad_chance
    for i in count_dict.values():
        print(i)
    Mx = discr_math_expectation(count_dict)
    Dx = discr_dispersion(count_dict)
    std = discr_standart_deviation(count_dict)
    answer +=f'12. M(x) = {Mx}, D(x) = {Dx}, Оклонение = {std}'
    return text, answer
