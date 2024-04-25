from random import randint
from random import uniform
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
        answer += f'{green}/{green + purple} * {green - 1}/{green + purple - 1} или '\
            f'{round(green /(green + purple) * (green - 1)/(green + purple - 1), 4)} '
    elif type == 1:
        answer += f'{purple}/{green + purple} * {purple - 1}/{green + purple - 1} или '\
            f'{round(purple /(green + purple) * (purple - 1)/(green + purple - 1), 4)} '
    else:
        answer += f'{purple}/{green + purple} * {green}/{green + purple - 1} + '\
            f'{green}/{green + purple} * {purple}/{green + purple - 1} или '\
            f'{round((purple/(green + purple) * green/(green + purple - 1)*2), 4) }'
    text += f'Ответ: {answer}'
    return text
