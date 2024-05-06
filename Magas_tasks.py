

from math import sqrt
from functions import integr_lapl, local_lapl
from random import randint, randrange

'''
def myFunction():
    pass
def getEntry():
    value = data.get()
    print(value)


import tkinter as tk
win = tk.Tk()
win.title("Задачи по теории вероятности")
win.geometry("650x250+400+200")

label1 = tk.Label(win,text = "Выберите вариант(ы):",font=("Arial", 12));
label2 = tk.Label(win,text = "Выберите номера задач:",font=("Arial", 12));
label3 = tk.Label(win,text = "Введите необходимое число вариантов:",font=("Arial", 12));

data = tk.Entry(win,width=5)

checkbox1_1 = tk.Checkbutton(win,text="13",font=("Arial", 12))
checkbox1_2 = tk.Checkbutton(win,text="14",font=("Arial", 12))
checkbox1_3 = tk.Checkbutton(win,text="15",font=("Arial", 12))

checkbox2_1 = tk.Checkbutton(win,text="все",font=("Arial", 12))

tasks = []

for i in range(0,22):
    checkbox2 = tk.Checkbutton(win,text=i+1,font=("Arial", 12))
    checkbox2.grid(row=2+i//6,column=2+i%6,stick="w")
    tasks.append(checkbox2)


btn1 = tk.Button(win, text= "Создать",
                 command=getEntry,
                 activebackground="blue",font=("Arial", 12))



label1.grid(row=0,column=0,columnspan=2,stick="w")
label2.grid(row=1,column=0,columnspan=2,stick="w")
label3.grid(row=6,column=0,columnspan=2,stick="w")

data.grid(row=6,column=2,stick="w")

checkbox1_1.grid(row=0,column=2,stick="w")
checkbox1_2.grid(row=0,column=3,stick="w")
checkbox1_3.grid(row=0,column=4,stick="w")

checkbox2_1.grid(row=1,column=2,stick="w")

btn1.grid(row=8,column=7)


win.mainloop()
'''


def task_1():
    task = "1. "
    task += "Домашняя обезьянка бьет лапой по клавишам пишущей машинки "
    arr = ["А", "О", "Е", "И", "У", "Ю"]
    answer = "1. "
    if (randint(0, 1)):
        task += "пять раз. Какова вероятность, что напечатанные буквы:\n"
        task += "\tа) составят имя её хозяина «"
        arr_1 = ["Сидор", "Артур", "Остап", "Гарри", "Захар", "Аммар", "Ермак", "Назар", "Афоня", "Тарас"]
        task += arr_1[randint(0, 9)] + "»;\n"
        task += "\tб) образуют слово, начинающееся с буквы «"
        task += arr[randint(0, 5)] + "»?\n"
        answer += "a) 1/(33)^5\tb) 1/33\n"
    else:
        task += "шесть раз. Какова вероятность, что напечатанные буквы:\n"
        task += "\tа) составят имя её хозяйки «"
        arr_1 = ["Аврора", "Галина", "Инесса", "Любовь", "Милана", "Селена", "Эмилия", "Джулия", "Анжела", "Шакира"]
        task += arr_1[randint(0, 9)] + "»;\n"
        task += "\tб) образуют слово, начинающееся и заканчивающееся буквой «"
        task += arr[randint(0, 5)] + "»?\n"
        answer += "a) 1/(33)^6\tb) 1/(33)^2\n"
    task_and_answer = [task, answer]
    return task_and_answer


def task_2():
    task = "2. "
    task += "В группе из "
    answer = "2. "
    x1 = randint(5, 10)
    x2 = randint(5, 10)
    task += "тридцати человек "
    task += str(x1) + " выполнили домашнее задание полностью "
    task += str(x2) + " - частично, очтальные вообще не сделали его. "
    task += "Преподаватель берёт наугад пять тетрадей с домашним заданием. "
    task += "Найти вероятность того, что среди этих тетрадей:\n"

    task += "\tа) все пять — с выполненным полностью домашним заданием;\n"
    task += "\tб) две — с частично выполненным заданием и две — вообще без домашнего задания."

    answer += "a) C(из " + str(x1) + " по 5) " + "\tb) C(из " + str(x2) + " по 2) * " + "C(из " + str(
        30 - x1 - x2) + " по 2) * " + "C(из " + str(26) + " по 1)  /  C(из 30 по 5)\n"
    task_and_answer = [task, answer]
    return task_and_answer


def task_3():
    task = "3. "
    task += "Вероятность сняться в рекламе университета путей сообщения для первокурсника равна "
    answer = "3. "
    x1 = randint(5, 9) / 10
    x2 = randint(1, 4) / 10
    task += str(x1) + ", для пятикурсника — "
    task += str(
        x2) + ". Чему равна вероятность того, что во время очередной рекламной паузы университет будут прославлять:\n"
    task += "\tа) оба студента;\n"
    task += "\tб) только первокурсник;\n"
    task += "\tв) кто-нибудь из них?\n"

    answer += "a) " + str(round(x1 * x2, 2)) + "\tб) " + str(round(x1 * (1 - x2), 2)) + "\tв) " + str(
        round(x1 * x2 + x1 * (1 - x2) + (1 - x1) * x2, 2))+"\n"
    task_and_answer = [task, answer]
    return task_and_answer


def task_4():
    task = "4. "
    task += "Два лаборанта делают измерения некоторой физической величины. "
    task += "Вероятность допустить ошибку при снятии показания для первого сотрудника равна "
    answer = "4. "
    x1 = randint(1, 9) / 10
    q1 = round(1 - x1, 4)
    x2 = randint(1, 9) / 10
    q2 = round(1 - x2, 4)
    task += str(x1) + ", для второго — "
    task += str(
        x2) + ". Каждый лаборант сделал по два измерения.Какова вероятность, что ошибочных измерений у них поровну?\n"

    answer += str(round(x1 * x1 * x2 * x2, 4) + round(x1 * q1 * x2 * q2, 4) + round(q1 * q1 * q2 * q2, 4))
    task_and_answer = [task, answer]
    return task_and_answer


def task_5():
    task = "5. "
    x = randint(10, 15)
    k = randint(3, x - 5)
    task += "В группе 14д механического факультета из 25 студентов " + str(
        x) + " не подготовились к занятию по математике."
    task += "Найти вероятность того, что " + str(k) + " случайно выбранных студентов оказались подготовленными."
    answer = "5. "

    answer += "C(из " + str(25 - x) + " по " + str(k) + ") / C(из 25 по " + str(k) + ")\n"
    task_and_answer = [task, answer]
    return task_and_answer


def task_6():
    task = "6. "
    ph1 = randint(1, 8) / 10
    ph2 = randint(1, 9 - ph1 * 10) / 10
    ph3 = round(1 - ph1 - ph2, 2)
    p1 = randint(1, 4) / 10
    p2 = randint(1, 4) / 10
    p3 = randint(1, 4) / 10
    task += "В ювелирной лавке " + str(int(ph1 * 100)) + "% изделий украшены горным "
    task += "хрусталем (бесцветный кварц), " + str(int(ph2 * 100)) + "% — аметистом (фиолетовый кварц), " + str(
        int(ph3 * 100)) + "% — морионом (черный кварц). "
    task += "Производство ювелирных украшений таково, что вероятность попадания в кварц двойников, образующих зернистые "
    task += "кристаллы, для горного хрусталя равна " + str(p1) + ", для аметиста — " + str(
        p2) + ", для мориона — " + str(p3) + ". "
    task += "Не искушенная в ювелирном искусстве юная барышня выбирает украшение случайным образом."
    task += " Какова вероятность того, что оно не будет содержать примеси двойника?"
    answer = "6. "

    pah1 = 1 - p1
    pah2 = 1 - p2
    pah3 = 1 - p3

    pa = ph1 * pah1 + ph2 * pah2 + ph3 * pah3

    answer += str(round(pa, 2))+"\n"
    task_and_answer = [task, answer]
    return task_and_answer


def task_7():
    task = "7. "
    n1 = randint(5, 12) * 90
    n2 = randint(5, 12) * 90
    n3 = 3000 - n1 - n2
    p1 = randint(5, 15) / 100
    p2 = randint(5, 15) / 100
    p3 = randint(5, 15) / 100
    task += "В магазин поступили ботинки с трех обувных фабрик: " + str(n1) + " пар с фабрики «Большевик», " + str(n2)
    task += " пар с фабрики «Пионер» и " + str(n3) + " с фабрики «Комсомолец»."
    task += " Вероятность для этих фабрик выпустить бракованную обувь равна " + str(p1) + ", " + str(p2) + " и " + str(
        p3) + " соответственно."
    task += "Беспечный покупатель купил ботинки наудачу. Через неделю у правого ботинка отвалилась подошва."
    task += " На какой фабрике вероятнее всего были сделаны эти ботинки?"
    answer = "7. "

    ph1 = n1 / 3000
    ph2 = n2 / 3000
    ph3 = n3 / 3000

    pa = p1 * ph1 + p2 * ph2 + p3 * ph3

    ph1a = p1 * ph1 / pa
    ph2a = p2 * ph2 / pa
    ph3a = p3 * ph3 / pa

    answer += str(round(max(ph1a, ph2a, ph3a), 2))+"\n"
    task_and_answer = [task, answer]
    return task_and_answer


def task_8():
    task = "8. "
    p = randint(1, 9) / 10
    task += "Событие В произойдет в случае, если событие А наступит не менее четырех раз. Найти вероятность события"
    task += " В, если производится пять независимых испытаний, в каждом из которых вероятность совершения А равна " + str(
        p) + "."

    answer = "8. "

    answer += str("C(из 5 по 4) * " + str(p) + "^4 * " + str(1 - p) + "+ C(из 5 по 5) * " + str(p) + "^5 = " + str(
        round(pow(p, 5) + 4 * pow(p, 4), 5)))+"\n"
    task_and_answer = [task, answer]
    return task_and_answer


def task_9():
    task = "9. "
    n = 100
    k = 50
    k1 = 100
    p = randint(40, 60) / 100
    task += "Вероятность изготовления детали номинальных размеров равна " + str(
        p) + ". Найти вероятность того, что среди "
    task += "100 деталей окажется:\n"
    task += "\tа) половина деталей номинальных размеров;\n"
    task += "\tб) не менее половины таких деталей."

    answer = "9. "

    x = (k - n * p) / sqrt(n * p * (1 - p))
    x2 = (k1 - n * p) / sqrt(n * p * (1 - p))

    answer += "a) " + str(round(float(local_lapl(round(x, 1))) / sqrt(n * p * (1 - p)), 3))
    answer += "\tб)" + str(round(float(integr_lapl(round(x2, 2))) - float(integr_lapl(round(x, 2))), 3))+"\n"

    task_and_answer = [task, answer]
    return task_and_answer


def task_10():
    task = "10. "
    n = randint(3, 7) * 100
    p = randint(3, 7) / 1000
    k = 5
    task += "Среди семян ржи " + str(p * 100) + "% семян сорняков. Какова вероятность при случайном наборе " + str(
        n) + " семян обнаружить пять семян сорняков?"

    answer = "10. "

    x = (k - n * p) / sqrt(n * p * (1 - p))
    answer += str(round(float(local_lapl(round(x, 1))) / sqrt(n * p * (1 - p)), 3)) + "\n"

    task_and_answer = [task, answer]
    return task_and_answer


def task_11():
    task = "11. "

    p = randint(1, 9) / 10
    q = round(1 - p, 1)

    task += "Вероятность производства нестандартного изделия равна " + str(
        q) + " . Контролер проверяет не более пяти изделий из"
    task += " партии. Если изделие оказывается нестандартным, испытания прекращаются, а партия бракуется. Если изделие"
    task += " оказывается стандартным, контролер берет следующее и т. д. Составить ряд распределения числа проверенных"
    task += " изделий. Найти М(Х), D(X), σ(X), F(X) этой случайной величины. Построить график F(X)."

    answer = "11. "

    p1 = round(q, 1)
    p2 = round(p * q, 2)
    p3 = round(p * p * q, 3)
    p4 = round(p * p * p * q, 4)
    p5 = round(p * p * p * p, 4)

    answer += "Ряд распределения: \nxi\t1\t2\t3\t4\t5\n"
    answer += "pi\t" + str(p1) + "\t" + str(p2) + "\t" + str(p3) + "\t" + str(p4) + "\t" + str(p5) + "\n\n"
    M = 1 * p1 + 2 * p2 + 3 * p3 + 4 * p4 + 5 * p5
    answer += "M(X) = " + str(M) + "\t"
    D = round(1 * p1 + 4 * p2 + 9 * p3 + 16 * p4 + 25 * p5 - M ** 2, 3)
    answer += "D(X) = " + str(D) + "\t"
    Q = round(sqrt(D), 3)
    answer += "σ(X) = " + str(Q) + "\n"
    F = "\t__________\n"
    F += "\t| 0\t, x<=1\n"
    F += "\t| " + str(round(p1, 1)) + "\t, 1<x≤2\n"
    F += "F(X) =\t| " + str(round(p1 + p2, 2)) + "\t, 2<x≤3\n"
    F += "\t| " + str(round(p1 + p2 + p3, 3)) + " , 3<x≤4\n"
    F += "\t| " + str(round(p1 + p2 + p3 + p4, 4)) + ", 4<x≤5\n"
    F += "\t| 1\t, 5<x\n"
    F += "\t‾‾‾‾‾‾‾‾‾‾"
    answer += F+"\n"
    task_and_answer = [task, answer]
    return task_and_answer


def task_12():
    task = "12. "

    n = 3
    p = randint(1, 9) / 10
    q = round(1 - p, 1)

    task += "Производится три независимых опыта, в каждом из которых событие появляется с вероятностью " + str(
        p) + " . Составить"
    task += "ряд распределения числа появлений события в трех опытах. Найти M(X) и D(X) этой случайной величины."

    answer = "12. "

    p0 = round(q * q * q, 3)
    p1 = round(3 * p * q * q, 3)
    p2 = round(3 * p * p * q, 3)
    p3 = round(p * p * p, 3)

    answer += "Ряд распределения: \nxi\t0\t1\t2\t3\n"
    answer += "pi\t" + str(p0) + "\t" + str(p1) + "\t" + str(p2) + "\t" + str(p3) + "\n\n"
    M = round(n * p, 1)
    answer += "M(X) = " + str(M) + "\t"
    D = round(n * p * q, 2)
    answer += "D(X) = " + str(D) + "\n"

    task_and_answer = [task, answer]
    return task_and_answer


def task_13():
    task = "13. "
    r = randint(1, 3)
    n = 0
    if r == 1:
        n = 1000
    elif r == 2:
        n = 2000
    else:
        n = 10000

    p = 1 / n

    task += "Устройство содержит " + str(n) + " одинаково надежных элементов, вероятность отказа каждого из них равна "
    task += str(p) + ". Составить ряд распределения числа отказавших элементов. Найти M(X) этой случайной величины."

    answer = "13. "

    answer += "Ряд распределения: \nxi\t0\t1\t\t2\t\t\t...\tk\t\t\t...\tn\n"
    answer += "pi\te^(-λ)\tλ*e^(-λ)\t((λ^2)/2)*e^(-λ)\t...\t((λ^k)/k)*e^(-λ)\t...\t((λ^n)/n)*e^(-λ)\n\n"
    answer += ",где n = " + str(n) + "\tp = " + str(p) + "\tλ = n * p = " + str(n * p) + "\n\n"
    M = n * p
    answer += "M(X) = n * p = " + str(M) + "\n"

    task_and_answer = [task, answer]
    return task_and_answer


def task_14():
    task = "14. "

    task += "Независимые случайные величины X и Y заданы таблицами распределений.\n"
    task += "Найти:\n"
    task += "\t1) M(X), M(Y), D(X), D(Y);\n"
    task += "\t2) таблицы распределения случайных величин Z1 = 2X + Y, Z2 = X * Y;\n"
    task += "\t3) M(Z1), M(Z2), D(Z1), D(Z2) непосредственно по таблицам распределений"
    task += "и на основании свойств математического ожидания и дисперсии.\n"

    # Таблицы X и Y
    xi = ["-1", "1", "2"]
    pxi = ["p", "0.1", "0.3"]

    yi = ["2", "4"]
    pyi = ["0.4", "0.6"]

    # Тут надо как-то в условие закинуть таблицы X и Y
    task += f'X:\t{xi[0]}\t{xi[1]}\t{xi[2]}\n'
    task += f'P:\t{pxi[0]}\t{pxi[1]}\t{pxi[2]}\n'
    task += '\n'
    task += f'Y:\t{yi[0]}\t{yi[1]}\n'
    task += f'P:\t{pyi[0]}\t{pyi[1]}\n'

    answer = "14. "

    answer += "1) M(X) = 0.1\tD(X) = 1.89\tM(Y) = 3.2\tD(Y) = 0.96\n"

    answer += "2)\n"

    # Таблицы Z1 и Z2
    zi1 = ["0", "2", "4", "6", "8"]
    pzi1 = ["0.24", "0.36", "0.04", "0.18", "0.18"]

    zi2 = ["-4", "-2", "2", "4", "8"]
    pzi2 = ["0.36", "0.24", "0.04", "0.18", "0.18"]

    # Тут надо как-то в ответ закинуть таблицы Z1 и Z2
    answer += f'Z1:\t{zi1[0]}\t{zi1[1]}\t{zi1[2]}\t{zi1[3]}\n'
    answer += f'P:\t{pzi1[0]}\t{pzi1[1]}\t{pzi1[2]}\t{pzi1[3]}\n'
    answer += '\n'
    answer += f'Z1:\t{zi2[0]}\t{zi2[1]}\t{zi2[2]}\t{zi2[3]}\t{zi2[4]}\n'
    answer += f'P:\t{pzi2[0]}\t{pzi2[1]}\t{pzi2[2]}\t{pzi2[3]}\t{pzi2[4]}\n'

    answer += "\n3) M(Z1) = M(2X+Y) = 2 * M(X) + M(Y) = 2 * 0.1 + 3.2 = 3.4\n   D(Z1) = D(2X+Y) = 4 * D(X) + D(Y) = 4 * 1.89 + 0.96 = 8.52\n"
    answer += "   M(Z2) = M(X*Y) = M(X) * M(Y) = 0.1 * 3.2 = 0.32\n"
    answer += "   D(Z2) = M( (Z2)^2 ) - M(Z2)^2 = 16 * 0.36 + 4 * 0.24 + 4 * 0.04 + 16 * 0.18 + 64 * 0.18 - 0.1024 = 21.1776\n"

    task_and_answer = [task, answer]
    return task_and_answer


def task_15():
    task = "15. "

    a = randint(11, 14) / 10
    b = randint(15, 19) / 10

    F = "\t__________\n"
    F += "\t| 0\t\t, x≤1\t\tα = " + str(a) + "\n"
    F += "F(X) =\t| (x^2-x)/2\t, 1<x≤2\tβ = " + str(b) + "\n"
    F += "\t| 1\t\t, 2<x\n"
    F += "\t‾‾‾‾‾‾‾‾‾‾"

    task += "Дана функция распределения F(x) непрерывной случайной величины X.\nТребуется:\n"
    task += "\t1) найти плотность вероятности f(x);\n"
    task += "\t2) построить графики F(x) и f(x);\n"
    task += "\t3) найти M(X), D(X), σ(Х);\n"
    task += "\t4) найти Р(α < X < β) для данных α, β.\n"
    task += F

    answer = "15. "

    f = "\t__________\n"
    f += "\t| 0\t\t, x≤1\n"
    f += "f(X) =\t| x-(1/2)\t, 1<x≤2\n"
    f += "\t| 0\t\t, 2<x\n"
    f += "\t‾‾‾‾‾‾‾‾‾‾\n"

    answer += "1)" + f
    answer += "3) M(x) = 1.58\tD(x) = 0.076\tσ(x) = 0.076\n"
    answer += "4) P(" + str(a) + "<x<" + str(b) + ") = F(" + str(b) + ")-F(" + str(a) + ") = " + str(
        round(((b * b - b) - (a * a - a)) / 2, 3)) + "\n"

    task_and_answer = [task, answer]
    return task_and_answer


'''
А я старался... а я делал... плак-плак-плак
def task_16():
    task = "Задача №16\n"

    f ="\t__________\n"
    f+="\t| 0\t\t, x<0\n"
    f+="f(X) =\t| a * (2x+1)\t, 0≤x≤1\n"
    f+="\t| 0\t\t, 1<x\n"
    f+="\t‾‾‾‾‾‾‾‾‾‾\n"

    task += "Дана плотность вероятности f(x) непрерывной случайной величины X.\nТребуется:\n"
    task += "\t1) найти параметр a;\n"
    task += "\t2) найти функцию распределения F(x);\n"
    task += "\t3) построить графики f(x) и F(x);\n"
    task += "\t4) найти асимметрию и эксцесс X.\n"
    task += f

    answer = ""

    F ="\t__________\n"
    F+="\t| 0\t\t, x<0\n"
    F+="F(X) =\t| (x^2+x)/2\t, 0≤x≤1\n"
    F+="\t| 1\t\t, 1<x\n"
    F+="\t‾‾‾‾‾‾‾‾‾‾\n"

    answer = "1) a = 1\n"
    answer += "2) "+F
    answer += "4) асимметрия = -0.007; эксцесс = 0.011 .\n"

    task_and_answer=[task,answer]
    return task_and_answer
'''


def task_16():
    task = "16. "

    a = randint(-5, -3)
    b = randint(1, 100)

    f = "\t__________\n"
    f += "\t| 0\t\t, x≤-6\t\tα = " + str(a) + "\n"
    f += "f(X) =\t| (2x+1) / 9\t, -6<x≤-3\tβ = " + str(b) + "\n"
    f += "\t| -x / 9\t, -3<x≤0\n"
    f += "\t| 0\t\t, 0<x\n"
    f += "\t‾‾‾‾‾‾‾‾‾‾\n"

    task += "Дана плотность вероятности f(x) непрерывной случайной величины X, имеющая две ненулевые составляющие формулы.\nТребуется:\n"
    task += "\t1) проверить свойство: интеграл f(x) на промежутке (-∞,+∞) = 1 ;\n"
    task += "\t2) построить график f(x);\n"
    task += "\t3) найти функцию распределения F(x)\n"
    task += "\t4) найти Р(α < X < β) для данных α, β.\n"
    task += "\t5) найти М(Х), D(X), σ(X).\n"
    task += f

    answer = "16. "

    F = "\t__________\n"
    F += "\t| 0\t\t, x≤-6\n"
    F += "F(X) =\t| (x^2+12x+36)/18, -6<x≤-3\n"
    F += "\t| 1 - (x^2/18)\t, -3<x≤0\n"
    F += "\t| 1\t\t, 0<x\n"
    F += "\t‾‾‾‾‾‾‾‾‾‾\n"

    answer += "1) свойство выполняется\n"
    answer += "3) " + F
    answer += "4) P(" + str(a) + "<x<" + str(b) + ") = F(" + str(b) + ")-F(" + str(a) + ") = " + str(
        round(1 - ((a * a + 12 * a + 36) / 18), 3)) + "\n"
    answer += "5) M(X) = -3\tD(X) = 1.5\tσ(X) = 1.22\n"

    task_and_answer = [task, answer]
    return task_and_answer


def task_17():
    task = "17. "

    n = 5 if randint(0, 1) else 10
    arr = ["одну минуту", "две минуты", "три минуты", "четыре минуты"]
    t = randint(0, 3)
    s = arr[t]

    task += f'Интервал движения трамвая равен {n} мин. Пассажир подходит к остановке в некоторый момент времени.'
    task += " Какова вероятность того, что он подошел не ранее чем через минуту после ухода предыдущего трамвая, "
    task += f"но не позднее, чем за {s} до отхода следующего?"

    answer = "17. "

    answer += str((n - 2 - t) / 10)
    task_and_answer = [task, answer]
    return task_and_answer


def task_18():
    task = "18. "

    a0 = randint(1, 10)
    b0 = randint(13, 24)
    a1 = randint(a0, 11)
    b1 = randint(12, b0)

    task += f'Все значения равномерно распределенной случайной величины X лежат на отрезке [{a0}; {b0}]. '
    task += f'Какова вероятность события: X принадлежит [{a1}; {b1}]?'

    answer = "18. "

    answer += str(round((b1 - a1) / (b0 - a0), 3)) + "\n"
    task_and_answer = [task, answer]
    return task_and_answer


def task_19():
    task = "19. "

    m = randrange(35, 45, 5)
    q = 5
    x1 = randint(20, 30)
    x2 = randint(35, 50)

    task += f'Случайная величина X имеет нормальное распределение с математическим '
    task += f'ожиданием m = {m} и σ = 5. Построить график плотности вероятности f(x) и '
    task += f'сравнить вероятности попадания X в интервалы (0; {x1}) и ({x2}; 55).\n'

    answer = "19. "

    answer += f'Точка максимума: ({m}, 1/({q}*√2π)) ; Точки перегиба: ({m - q}, 1/({q}*√2πe)), (({m + q}, 1/({q}*√2πe)))\n'
    P1 = float(integr_lapl((x1 - m) / 5) - integr_lapl((-m) / 5))
    P1 = round(P1, 4)
    P2 = float(integr_lapl((55 - m) / 5) - integr_lapl((x2 - m) / 5))
    P2 = round(P2, 4)
    answer += f'P(0<X<{x1}) = {P1}\t'
    answer += f'P({x2}<X<55) = {P2}\n'
    answer += f'P(0<X<{x1})<P({x2}<X<55)' if P1 < P2 else f'P(0<X<{x1})>P({x2}<X<55)\n'
    task_and_answer = [task, answer]
    return task_and_answer


def task_20():
    task = "20. "

    n = randrange(35, 45, 5)
    m0 = 50
    y0 = randrange(10, 20, 2)
    a = 1500 if randint(0, 1) else 2000
    b = a + 500

    task += f'Измерительная система состоит из {n} одинаковых датчиков. Время безотказной работы i-го датчика Ti '
    task += f'имеет нормальное распределение (m = {m0} ч; σ = {y0} ч), одинаковое для всех датчиков. В случае отказа i-го '
    task += f'датчика происходит мгновенное и безотказное переключение на следующий. Если отказали все датчики, то '
    task += f'измерительная система выходит из строя. С какой вероятностью измерительная система проработает до выхода '
    task += f'из строя от {a} до {b} ч? \n'

    answer = "20. "

    m = n * m0
    D = n * y0 * y0
    y = round(sqrt(D), 2)

    P = float(integr_lapl(round((b - m) / y, 2)) - integr_lapl(round((a - m) / y, 2)))
    P = round(P, 4)
    answer += f'm = M(T) = M(ΣTi) = n * m0 = {m}\t'
    answer += f'D(T) = D(ΣTi) = n * σ0^2 = {D} \t'
    answer += f'σ = √D(T) = {y} \n\n'
    answer += f'P({a}<X<{b}) = Ф( ({b}-{m}) / {y}) - Ф( ({a}-{m}) / {y}) = {P}\n'

    task_and_answer = [task, answer]
    return task_and_answer


#check = task_20()

#print(check[0])
#print(check[1])
