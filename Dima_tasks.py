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


def task_1():
    answer = '1. \n'
    text = "1. Студент забыл четырехзначный идентификационный код своей кредитной карточки." \
           "Какова вероятность того, что студент получит стипендию, набирая код наудачу, если он помнит, что:\n"
    k = randint(1, 2)
    if k == 1:
        text += "a)Все цифры кода разные\n"
        otvet1 = 1 / (10 * 9 * 8 * 7)
        answer += f"а) {otvet1}, 1/{10 * 9 * 8 * 7}\n"
    if k == 2:
        text += "a)Цифры в коде могут повторяться\n"
        otvet1 = 1 / 10000
        answer+= f"а) {otvet1}, 1/10000\n"
    chisl1 = randint(0, 9)
    chisl2 = randint(0, 9)
    while chisl1 == chisl2:
        chisl2 = randint(0, 9)
    text += f"б) код не содержит цифр {chisl1} и {chisl2}?\n"
    otvet2 = 1 / (8 * 8 * 8 * 8)
    answer += f"б) {otvet2}, 1/{8 * 8 * 8 * 8}\n"
    return text, answer


def task_2():
    answer = '2. \n'
    posilki = randint(10, 20)
    zima = randint(3, 4)
    otkrito = randint(2, 4)
    text = f"2. В детский дом города Алдан пришло {posilki} посылок из академии." \
           f'В {zima} из них — зимние вещи, в 1 — кожаный пиджак, в остальных — книги.' \
           f"Наугад открывают {otkrito} посылки. Какова вероятность того, что:\n"

    text += f"a) В {otkrito - 1} из них — зимние вещи и в 1 — кожаный пиджак;\n"
    i1 = otkrito
    i2 = zima
    i3 = posilki
    otvet = 1
    while i1 != 1:
        otvet *= i2 / i3
        i3 -= 1
        i2 -= 1
        i1 -= 1
    otvet *= 1 / i3
    answer += f"а) {otvet * otkrito}\n"

    text += f"б) Все {otkrito} с книгами\n"
    answer += f"б) {combination(posilki - zima - 1, otkrito)[1]}/{combination(posilki, otkrito)[1]}\n"
    return text, answer


def task_3():
    answer = '3. \n'
    c1 = randint(7, 9) / 10
    c2 = randint(5, 7) / 10

    text = f"3. Вероятность правильно ответить на вопрос в телевизионной игре «Кто хочет стать миллионером?» для инженера равна {c1}," \
           f'для экономиста — {c2}. \nКакова вероятность того, что на очередной вопрос ведущего:\n'
    k = randint(1, 2)
    if k == 1:
        text += "а) оба игрока ответят правильно;\n"
        answer+= f"а) {round(c1 * c2 * 100) / 100}\n"
    if k == 2:
        text += "а) оба игрока ответят неправильно;\n"
        answer += f"а) {round((1 - c1) * (1 - c2) * 100) / 100}\n"
    k = randint(1, 2)
    if k == 1:
        text += "б) хотя бы один из них даст правильный ответ;\n"
        answer += f"б) {round((c1 * c2 + (1 - c1) * c2 + c1 * (1 - c2)) * 100) / 100}\n"
    if k == 2:
        text += "б) хотя бы один из них даст неправильный ответ;\n"
        answer += f"б) {round(((1 - c1) * (1 - c2) + (1 - c1) * c2 + c1 * (1 - c2)) * 100) / 100}\n"
    k = randint(1, 2)
    if k == 1:
        text += "в) правильно ответит только экономист?\n"
        answer += f"в) {round((c2 * (1 - c1)) * 100) / 100}\n"
    if k == 2:
        text += "в) правильно ответит только инженер?\n"
        answer += f"в) {round(((1 - c2) * c1) * 100) / 100}\n"
    return text, answer


def task_4():
    answer = '4. \n'
    s1 = randint(1, 4)
    s2 = randint(2, 4)
    if s1 == s2:
        s2 = randint(2, 4)
    s3 = 10 - s1 - s2
    s1 = s1 / 10
    s2 = s2 / 10
    s3 = s3 / 10

    text = '4. Два гроссмейстера играют две партии в шахматы.' \
           f'Вероятность выигрыша в одной партии для первого шахматиста равна {s1}, для второго — {s2}; ' \
           f'вероятность ничьей — {s3}.' \
           'Какова вероятность того, что первый гроссмейстер выиграет матч?\n'

    otvet = s1 * s1 + s1 * s3 * 2
    answer += f'{round(otvet, 3)}\n'
    return text, answer


def task_5():
    answer = '5. \n'
    orange = randint(6, 9)
    purple = randint(4, 7)
    green = randint(1, 3)

    text = f'5. В урне {orange} оранжевых, {purple} фиолетовых и {green} зеленых шара.' \
           'Из урны трижды вынимают по одному шару, не возвращая их. ' \
           'Найти вероятность того, что при первом испытании появится оранжевый шар, ' \
           'при втором — фиолетовый,при третьем — зеленый.\n'
    vse = orange + purple + green
    otvet = (orange / vse) * (purple / (vse - 1)) * (green / (vse - 2))

    answer += f'({orange}/{vse})*({purple}/{vse - 1})*({green}/{vse - 2}),{otvet}\n'
    return text, answer


def task_6():
    answer = '6. \n'
    Ivanov = randint(3, 5) / 10
    Petrov = randint(4, 6) / 10
    Sidorov = randint(5, 7) / 10

    text = f'6. За нарушение правил игроками команды «Паровоз» в их ворота назначается одиннадцатиметровый удар.' \
           f'Лучшие футболисты команды «Тормоз» Иванов, Петров и Сидоров ' \
           f'забивают пенальти с вероятностью {Ivanov}, {Petrov} и {Sidorov} соответственно.' \
           'Найти вероятность того, что одиннадцатиметровый удар будет реализован, если пенальтиста выбирают по жребию.\n'
    otvet = (1 / 3) * Ivanov + (1 / 3) * Sidorov + (1 / 3) * Petrov
    otvet = round(otvet * 100) / 100
    answer += f'{otvet}\n'
    return text, answer


def task_7():
    answer = '7. \n'
    k1 = randint(2, 4) / 10
    k2 = randint(3, 5) / 10
    k3 = randint(1, 4) / 10
    k4 = randint(2, 5) / 10

    text = f'7. На старой граммофонной пластинке записаны произведения польского композитора и пианиста Фредерика' \
           'Шопена: концерт, соната, баллада и скерцо. Из-за частогопрослушивания пластинки дорожки стерлись,' \
           f'и звук воспроизводится некачественно во время проигрывания концерта с вероятностью {k1}, ' \
           f'сонаты — {k2}, баллады — {k3}, скерцо — {k4}. ' \
           'Звукосниматель наугад поставили на пластинку, музыка звучала чисто. Какова вероятность, что это была соната?\n'

    otvet = (1 / 4) * (1 - k2)
    answer += f'{otvet}\n'
    return text, answer


def task_8():
    answer = '8. \n'
    p = randint(2, 5)
    n = randint(4, 6)
    proc = randint(3, 5) * 10
    while (n / 100 * proc) % 1 != 0:
        proc = randint(3, 5) * 10
    text = f'8. Среди выпускаемых деталей бывает в среднем {p}% брака.' \
           f'Какова вероятность того, что среди взятых на испытание {n} деталей будет {proc}% бракованных?\n'
    k = n / 100 * proc
    p /= 100
    otvet = combination(n, int(k))[1] * p ** k * (1 - p) ** (n - k)
    answer += f'{round(otvet,5)}\n'

    return text, answer


def task_9():
    answer = '9. \n'
    p = randint(2, 4) / 10
    k1 = randint(30, 40)
    k2 = randint(10, 20)
    n = randint(400, 410)

    text = '9. Вероятность того, что деталь не пройдет проверку на качество,' \
           f'равна {p}. Какова вероятность того, что из {n} случайно отобранных деталей окажутся бракованными:\n' \
           f'а) {k1} деталей;\n' \
           f'б) от {k1+10} до {k1} деталей?\n'
    x=(k1-n*p)/(n*p*(1-p))
    y=(k1+10-n*p)/(n*p*(1-p))
    otvet = local_lapl(x)
    answer += f'a) {otvet}\n'
    answer += f'б) {round(integr_lapl(round(y,2))-integr_lapl(round(x,2)),5)}\n'
    return text, answer


def task_10():
    answer = '10. \n'
    n = randint(1200, 1500)
    k = randint(5, 15)
    p = randint(4, 9) / 1000

    text = f'10. Вероятность сбоя в работе АТС при каждом вызове равна {p}.' \
           f' Определить вероятность того, что при поступлении {n} вызовов произойдет {k} сбоев.\n'
    otvet = combination(n, k)[1] * p ** k * (1 - p) ** (n - k)
    answer += f'{round(otvet,5)}\n'
    return text, answer



def task_11():
    answer='11. \n'
    s1 = randint(85, 95) / 100
    s2 = randint(75, 85) / 100
    s3 = randint(65, 75) / 100
    s4 = randint(5, 6) / 10

    text = '11. Четыре студента повторно сдают экзамен. ' \
           f'Вероятность того, что сдаст экзамен первый студент, равна {s1}, второй — {s2}, третий — {s3}, четвертый — {s4}.' \
           'Составить ряд распределения числа студентов, которые сдадут экзамен. ' \
           'Найти М(Х), D(X), σ(X), F(X) этой случайной величины.\n'

    x0 = 0
    x1 = 1
    x2 = 2
    x3 = 3
    x4 = 4

    p0 = (1 - s1) * (1 - s2) * (1 - s3) * (1 - s4)
    p1 = s1 * (1 - s2) * (1 - s3) * (1 - s4) + (1 - s1) * s2 * (1 - s3) * (1 - s4) + (1 - s1) * (1 - s2) * s3 * (
                1 - s4) + (1 - s1) * (1 - s2) * (1 - s3) * s4
    p2 = s1 * s2 * (1 - s3) * (1 - s4) + s1 * (1 - s2) * s3 * (1 - s4) + s1 * (1 - s2) * (1 - s3) * s4 + (
                1 - s1) * s2 * s3 * (1 - s4) + (1 - s1) * s2 * (1 - s3) * s4 + (1 - s1) * (1 - s2) * s3 * s4
    p3 = (1 - s1) * s2 * s3 * s4 + s1 * (1 - s2) * s3 * s4 + s1 * s2 * (1 - s3) * s4 + s1 * s2 * s3 * (1 - s4)
    p4 = s1 * s2 * s3 * s4
    dictionary = {x0: round(p0, 5), x1: round(p1, 5), x2: round(p2, 5), x3: round(p3, 5), x4: round(p4, 5)}
    M = discr_math_expectation(dictionary)
    D = discr_dispersion(dictionary)
    S = discr_standart_deviation(dictionary)
    answer += f'M(X)={M}\nD(X)={D}\nσ ={S}\n'
    return text,answer


def task_12():
    answer = '12. \n'
    standart = randint(5, 7)
    unstandart = 10 - standart
    k = randint(2, 3)
    text = f"12. У сборщика десять деталей, среди которых {standart} стандартных и {unstandart} нестандартных." \
           f'Он наугад берет {k} детали. Составить ряд распределения числа стандартных деталей среди {k} отобранных.' \
           'Найти M(X) и D(X) этой случайной величины.\n'
    if k == 2:
        P0 = combination(standart, 0)[1] * combination(unstandart, 2)[1] / combination(10, 2)[1]
        P1 = combination(standart, 1)[1] * combination(unstandart, 1)[1] / combination(10, 2)[1]
        P2 = combination(standart, 2)[1] * combination(unstandart, 0)[1] / combination(10, 2)[1]
        dictinary = {0: P0, 1: P1, 2: P2}
        M = discr_math_expectation(dictinary)
        D = discr_dispersion(dictinary)
        answer += f"M(x)= {M}, D(x)={D}"
    else:
        P0 = combination(standart, 0)[1] * combination(unstandart, 3)[1] / combination(10, 3)[1]
        P1 = combination(standart, 1)[1] * combination(unstandart, 2)[1] / combination(10, 3)[1]
        P2 = combination(standart, 2)[1] * combination(unstandart, 1)[1] / combination(10, 3)[1]
        P3 = combination(standart, 3)[1] * combination(unstandart, 0)[1] / combination(10, 3)[1]
        dictinary = {0: P0, 1: P1, 2: P2, 3: P3}
        M = discr_math_expectation(dictinary)
        D = discr_dispersion(dictinary)
        answer += f"M(x)= {M}, D(x)={D}\n"
    return text, answer


def task_13():
    answer = '13. \n'
    n = randint(80, 100)
    k = randint(1, 5) / 100
    text = f"13. Вероятность появления события А в одном испытании равна {k}. " \
           f'Составить ряд распределения числа появлений события А в {n} испытаниях.\n' \
           'Найти M(X) этой случайной величины.\n'
    answer += "Ряд распределения:\n"
    M = n * k
    for i in range(0, 7):
        P = combination(n, i)[1] * k ** i * (1 - k) ** (n - i)
        answer += f'{P}\n'
    answer += '...\n'
    answer += f"M(x)={round(M, 5)}\n"
    return text, answer


def task_14():
    answer = '14. \n'
    text = '14. Независимые случайные величины X и Y заданы таблицами распределений.\n' \
           'Найти:\n' \
           '1) M(X), M(Y), D(X), D(Y);\n' \
           '2) таблицы распределения случайных величин Z1 = 2X+Y, Z2 = X  Y;\n' \
           '3) M(Z1), M(Z2), D(Z1), D(Z2) непосредственно по таблицам распределений и на основании свойств математического ожидания и дисперсии\n'
    p_x1 = randint(1, 3)
    p_x2 = randint(4, 6)
    p_x3 = 10 - p_x1 - p_x2
    p_x1 /= 10
    p_x2 /= 10
    p_x3 /= 10

    p_y1 = randint(1, 4)
    p_y2 = 10 - p_y1
    p_y1 /= 10
    p_y2 /= 10

    dictinary_x = {-2: p_x1, -1: p_x2, 3: p_x3}
    dictinary_y = {1: p_y1, 8: p_y2}

    text+=f'{dictinary_x}\n{dictinary_y}\n'

    answer += f'M(X)={discr_math_expectation(dictinary_x)}\n' \
            f'D(X)={discr_dispersion(dictinary_x)}\n' \
            f'M(Y)={discr_math_expectation(dictinary_y)}\n' \
            f'D(Y)={discr_dispersion(dictinary_y)}\n'
    dictinary_z1 = {-3: round(p_x1 * p_y1 * 100) / 100, 4: round(p_x1 * p_y2 * 100) / 100,
                            -1: round(p_x2 * p_y1 * 100) / 100, 6: round(p_x2 * p_y2 * 100) / 100,
                            7: round(p_x3 * p_y1 * 100) / 100, 14: round(p_x3 * p_y2 * 100) / 100}
    dictinary_z2 = {-2: round(p_x1 * p_y1 * 100) / 100, -16: round(p_x1 * p_y2 * 100) / 100,
                    -1: round(p_x2 * p_y1 * 100) / 100, -8: round(p_x2 * p_y2 * 100) / 100,
                    3: round(p_x3 * p_y1 * 100) / 100, 24: round(p_x3 * p_y2 * 100) / 100}
    answer += f'Z1: {dictinary_z1}\n' \
            f'Z2: {dictinary_z2}\n'

    dictinary_x = {-2: p_x1, -1: p_x2, 3: p_x3}
    dictinary_y = {1: p_y1, 8: p_y2}
    answer += f'M(Z1)={discr_math_expectation(dictinary_z1)}\n' \
            f'D(Z1)={discr_dispersion(dictinary_z1)}\n' \
            f'M(Z2)={discr_math_expectation(dictinary_z2)}\n' \
            f'D(Z2)={discr_dispersion(dictinary_z2)}\n'
    return text, answer


def task_15():
    answer = '15.\n'
    a = randint(1, 3)
    b = randint(2, 5)
    while a >= b:
        b = randint(2, 4)

    text = '15. Дана функция распределения F(x) непрерывной случайной величины X.\n' \
           'Требуется:\n' \
           '1) найти плотность вероятности f(x);\n' \
           '2) найти M(X), D(X), σ(Х);\n' \
           '3) найти Р(a < X < b) для данных a, b.\n' \
           '\nF(x)=\n{0, x<=0\nx^2/25, 0<x<=5\n1, x>5}\n'
    text += f'a={a}, b={b}\n'

    answer += '1) f(x)=\n{0, x<=0\n2x/25, 0<x<=5\n0,x>5}\n'
    answer += '\n2) M(X)=10/3\nD(X)=25/18\nσ=(5*√2)/6\n'
    answer += f'\n3) Р(a < X < b)={round(((b ** 2 / 25) - (a ** 2 / 25)) * 10000) / 10000}\n'

    return text, answer

def task_16():
    answer = '16.\n'
    a = randint(1, 3)
    b = randint(4, 5)

    text = '16. Дана плотность вероятности f(x) непрерывной случайной величины X, имеющая две ненулевые составляющие формулы.\n' \
           'Требуется:\n' \
           '1) проверить свойство интеграл f(x)dx от бесконечности до бесконечности = 1;\n' \
           '3) найти функцию распределения F(x);\n' \
           '4) найти Р(a<= Х <=b) для данных a,b;\n' \
           '5) найти М(Х), D(X), σ(X).\n' \
           '\nf(x)=\n' \
           '{0, x<=0\n' \
           '(2/15)x, 0<x<=3\n' \
           '-(1/5)x+1, 3<x<=5\n' \
           '0, x>5}\n' \
           f'a={a}, b={b}\n'

    otvet = ((1 / 15) * 3 ** 2 - (1 / 15) * a ** 2) + ((-b ** 2 / 10) + b - (-3 ** 2 / 10) + 3)

    answer +='1) Свойство выполняется;\n' \
            '\n2)F(X)=\n' \
            '{0, x<=0\n' \
            '5x^2/24, 0<x<=3\n' \
            '-x^2/10+x-21/10, 3<x<=5\n' \
            '1, x>5}\n' \
            f'\n3) Р(a<= Х <=b)={round(otvet,4)}\n' \
            '\n4)M(X)=40/15\n' \
            'D(X)=19/18\n' \
            'σ=sqrt(38)/6\n'

    return text, answer

def task_17():
    answer = '17.\n'
    x=randint(1450,1550)
    text=f'17. Автомат вытачивает стальные оси. Стандартная длина оси {x} мм. ' \
         f'Фактически же длина оси X является нормальной случайной величиной (m = {x} мм). ' \
         'При проверке большой партии изготовленных осей выяснилось,'\
         f'что {x-18} <= X <= {x+18} (мм). Какова вероятность того, что длина наугад взятой оси меньше {x-5} мм?\n'
    otvet=integr_lapl(round(x-5/18,2)-integr_lapl(round(-5/18,2)))
    answer+=f'{otvet}\n'
    return text, answer

def task_18():
    answer = '18.\n '
    l=randint(1,5)/100
    x=randint(150,200)
    text=f'18. Время T (в часах) безотказной работы элемента распределено по экспоненциальному закону с параметром {l}. ' \
         'Указать плотность вероятности f(t) случайной величины T, ' \
         'найти среднее время безотказной работы элемента. ' \
         f'С какой вероятностью элемент проработает безотказно не менее {x} ч?\n'
    answer+=f'Cреднее время безотказной работы элемента = {round(1/l,2)},\n '
    answer+=f'Вероятность проработает элемент безотказно не менее {x} = {round(math.exp(-l*x),5)}\n'

    return text, answer

def task_19():
    answer = '19.\n'

    m=randint(70,100)
    a=randint(10,30)

    text=f'19. Время формирования грузового поезда есть нормальная случайная величина с параметрами: m = {m} мин;' \
         f'σ = {a} мин. Какова вероятность того, что на формирование очередного поезда потребуется более двух часов?\n'

    z=(120-m)/a
    answer+=f'{round(1-integr_lapl(round(z,2)),5)}\n'
    return text,answer

def task_20():
    answer='20.\n'

    a=randint(6950,7050)
    b=randint(7950,8050)

    text='20. Измерительная система состоит из 750 идентичных датчиков. ' \
         f'Время безотказной работы i-го датчика Ti распределено экспоненциально (параметр λ =0,1 одинаковдля всех датчиков) ' \
         'и измеряется в часах. В случае отказа i-го датчика происходит мгновенное и безотказное переключение на следующий. ' \
         'Если отказали все датчики, то измерительная система выходит из строя. ' \
         f'Выполнить грубую оценку вероятности того, что измерительная системапроработает до выхода из строя от {a} до {b} ч. ' \
         'Каково среднее время работы отдельного датчика?\n'

    x1=(a-750*(1/0.1))/math.sqrt(750*(1/0.1)**2)
    x2=(b-750*(1/0.1))/math.sqrt(750*(1/0.1)**2)

    otvet=integr_lapl(round(x2,2))-integr_lapl(round(x1,2))
    answer+=f'{round(otvet,5)}\n'
    return text,answer
