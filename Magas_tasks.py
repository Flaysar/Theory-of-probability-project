# coding: utf-8

from math import sqrt
from functions import integr_lapl, local_lapl
from random import randint
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
    task = "Задача №1\n"
    task += "Домашняя обезьянка бьет лапой по клавишам пишущей машинки "
    arr = ["А","О","Е","И","У","Ю"]
    answer = ""
    if(randint(0,1)):
        task += "пять раз. Какова вероятность, что напечатанные буквы:\n"
        task +=  "\tа) составят имя её хозяина «"
        arr_1 = ["Сидор","Артур","Остап","Гарри","Захар","Аммар","Ермак","Назар","Афоня","Тарас"]
        task += arr_1[randint(0,9)]+"»;\n"
        task +=  "\tб) образуют слово, начинающееся с буквы «"
        task += arr[randint(0,5)]+"»?\n"
        answer = "a) 1/(33)^5\tb) 1/33"
    else:
        task += "шесть раз. Какова вероятность, что напечатанные буквы:\n"
        task +=  "\tа) составят имя её хозяйки «"
        arr_1 = ["Аврора","Галина","Инесса","Любовь","Милана","Селена","Эмилия","Джулия","Анжела","Шакира"]
        task += arr_1[randint(0,9)]+"»;\n"
        task +=  "\tб) образуют слово, начинающееся и заканчивающееся буквой «"
        task += arr[randint(0,5)]+"»?\n"
        answer = "a) 1/(33)^6\tb) 1/(33)^2"
    task_and_answer=[task,answer]
    return task_and_answer

def task_2():
    task = "Задача №2\n"
    task += "В группе из "
    answer = ""
    x1 = randint(5,10)
    x2 = randint(5,10)
    task += "тридцати человек "
    task += str(x1) +" выполнили домашнее задание полностью "
    task += str(x2) +" - частично, очтальные вообще не сделали его. "
    task += "Преподаватель берёт наугад пять тетрадей с домашним заданием. "
    task += "Найти вероятность того, что среди этих тетрадей:\n"
    
    task += "\tа) все пять — с выполненным полностью домашним заданием;\n"
    task += "\tб) две — с частично выполненным заданием и две — вообще без домашнего задания."

    answer = "a) C(из "+str(x1)+" по 5) "+"\tb) C(из "+str(x2)+" по 2) * "+"C(из "+str(30-x1-x2)+" по 2) * "+"C(из "+str(26)+" по 1)  /  C(из 30 по 5)"
    task_and_answer=[task,answer]
    return task_and_answer

def task_3():
    task = "Задача №3\n"
    task += "Вероятность сняться в рекламе университета путей сообщения для первокурсника равна "
    answer = ""
    x1 = randint(5,9)/10
    x2 = randint(1,4)/10
    task += str(x1) +", для пятикурсника — "
    task += str(x2) +". Чему равна вероятность того, что во время очередной рекламной паузы университет будут прославлять:\n"
    task += "\tа) оба студента;\n"
    task += "\tб) только первокурсник;\n"
    task += "\tв) кто-нибудь из них?\n"

    answer = "a) "+str(round(x1*x2, 2))+"\tб) "+str(round(x1*(1-x2), 2))+"\tв) "+str(round(x1*x2+x1*(1-x2)+(1-x1)*x2, 2))
    task_and_answer=[task,answer]
    return task_and_answer

def task_4():
    task = "Задача №4\n"
    task += "Два лаборанта делают измерения некоторой физической величины. "
    task += "Вероятность допустить ошибку при снятии показания для первого сотрудника равна "
    answer = ""
    x1 = randint(1,9)/10
    q1 = round(1-x1,4)
    x2 = randint(1,9)/10
    q2 = round(1-x2,4)
    task += str(x1) +", для второго — "
    task += str(x2) +". Каждый лаборант сделал по два измерения.Какова вероятность, что ошибочных измерений у них поровну?\n"

    answer = str(round(x1*x1*x2*x2, 4)+round(x1*q1*x2*q2,4)+round(q1*q1*q2*q2,4))
    task_and_answer=[task,answer]
    return task_and_answer

def task_5():
    task = "Задача №5\n"
    x = randint(10,15)
    k = randint(3,x-5)
    task += "В группе 14д механического факультета из 25 студентов "+str(x)+" не подготовились к занятию по математике."
    task += "Найти вероятность того, что "+str(k)+" случайно выбранных студентов оказались подготовленными."
    answer = ""

    answer = "C(из "+str(25-x)+" по "+str(k)+") / C(из 25 по "+str(k)+")"
    task_and_answer=[task,answer]
    return task_and_answer

def task_6():
    task = "Задача №6\n"
    ph1 = randint(1,8)/10
    ph2 = randint(1,9-ph1*10)/10
    ph3 = round(1-ph1-ph2,2)
    p1 = randint(1,4)/10
    p2 = randint(1,4)/10
    p3 = randint(1,4)/10
    task += "В ювелирной лавке "+str(int(ph1*100))+"% изделий украшены горным "
    task += "хрусталем (бесцветный кварц), "+str(int(ph2*100))+"% — аметистом (фиолетовый кварц), "+str(int(ph3*100))+"% — морионом (черный кварц). "
    task += "Производство ювелирных украшений таково, что вероятность попадания в кварц двойников, образующих зернистые "
    task += "кристаллы, для горного хрусталя равна "+str(p1)+", для аметиста — "+str(p2)+", для мориона — "+str(p3)+". "
    task += "Не искушенная в ювелирном искусстве юная барышня выбирает украшение случайным образом."
    task +=" Какова вероятность того, что оно не будет содержать примеси двойника?"
    answer = ""

    pah1 = 1 - p1
    pah2 = 1 - p2
    pah3 = 1 - p3
    
    pa = ph1*pah1+ph2*pah2+ph3*pah3

    answer = str(round(pa,2))
    task_and_answer=[task,answer]
    return task_and_answer

def task_7():
    task = "Задача №7\n"
    n1 = randint(5,12)*90
    n2 = randint(5,12)*90
    n3 = 3000-n1-n2
    p1 = randint(5,15)/100
    p2 = randint(5,15)/100
    p3 = randint(5,15)/100
    task += "В магазин поступили ботинки с трех обувных фабрик: "+str(n1)+" пар с фабрики «Большевик», "+str(n2)
    task += " пар с фабрики «Пионер» и "+str(n3)+" с фабрики «Комсомолец»."
    task += " Вероятность для этих фабрик выпустить бракованную обувь равна "+str(p1)+", "+str(p2)+" и "+str(p3)+" соответственно."
    task += "Беспечный покупатель купил ботинки наудачу. Через неделю у правого ботинка отвалилась подошва."
    task += " На какой фабрике вероятнее всего были сделаны эти ботинки?"
    answer = ""

    ph1 = n1/3000
    ph2 = n2/3000
    ph3 = n3/3000
    
    pa = p1*ph1+p2*ph2+p3*ph3
    
    ph1a = p1*ph1/pa
    ph2a = p2*ph2/pa
    ph3a = p3*ph3/pa

    answer = str(round(max(ph1a,ph2a,ph3a),2))
    task_and_answer=[task,answer]
    return task_and_answer

def task_8():
    task = "Задача №8\n"
    p = randint(1,9)/10
    task += "Событие В произойдет в случае, если событие А наступит не менее четырех раз. Найти вероятность события"
    task += " В, если производится пять независимых испытаний, в каждом из которых вероятность совершения А равна "+str(p)+"."
    
    answer = ""

    answer = str("C(из 5 по 4) * "+str(p)+"^4 * "+str(1-p)+"+ C(из 5 по 5) * " + str(p)+"^5 = "+str(round(pow(p,5)+4*pow(p,4),5)))
    task_and_answer=[task,answer]
    return task_and_answer

def task_9():
    task = "Задача №9\n"
    n=100
    k=50
    k1=100
    p = randint(40,60)/100
    task += "Вероятность изготовления детали номинальных размеров равна "+str(p)+". Найти вероятность того, что среди "
    task += "100 деталей окажется:\n"
    task += "\tа) половина деталей номинальных размеров;\n"
    task += "\tб) не менее половины таких деталей."
    
    answer = ""
    
    x = (k-n*p)/sqrt(n*p*(1-p))
    x2 = (k1-n*p)/sqrt(n*p*(1-p))
    
    answer = "a) "+str(round(float(local_lapl(round(x,1)))/sqrt(n*p*(1-p)),3))
    answer +="\tб)"+str(round(float(integr_lapl(round(x2,2)))-float(integr_lapl(round(x,2))),3))
    
    task_and_answer=[task,answer]
    return task_and_answer

def task_10():
    task = "Задача №10\n"
    n= randint(3,7)*100
    p = randint(3,7)/1000
    k=5
    task += "Среди семян ржи "+str(p*100)+"% семян сорняков. Какова вероятность при случайном наборе "+str(n)+" семян обнаружить пять семян сорняков?"
    
    answer = ""
    
    x = (k-n*p)/sqrt(n*p*(1-p))
    print(str(n)+"\t"+str(p)+"\t"+str(x))
    answer = str(round(float(local_lapl(round(x,1)))/sqrt(n*p*(1-p)),3))
    
    task_and_answer=[task,answer]
    return task_and_answer

def task_11():
    task = "Задача №11\n"
    
    p = randint(1,9)/10
    q = round(1 - p,1)

    task += "Вероятность производства нестандартного изделия равна "+str(q)+" . Контролер проверяет не более пяти изделий из"
    task += " партии. Если изделие оказывается нестандартным, испытания прекращаются, а партия бракуется. Если изделие"
    task += " оказывается стандартным, контролер берет следующее и т. д. Составить ряд распределения числа проверенных"
    task += " изделий. Найти М(Х), D(X), Q(X), F(X) этой случайной величины. Построить график F(X)."
    
    answer = ""
    
    p1 = round(q,1)
    p2 = round(p * q,2)
    p3 = round(p * p * q,3)
    p4 = round(p * p * p * q,4)
    p5 = round(p * p * p * p,4)
    

    print()
    answer = "Ряд распределения: \nxi\t1\t2\t3\t4\t5\n"
    answer += "pi\t"+str(p1)+"\t"+str(p2)+"\t"+str(p3)+"\t"+str(p4)+"\t"+str(p5)+"\n\n"
    M = 1*p1+2*p2+3*p3+4*p4+5*p5
    answer += "M(X) = "+str(M)+"\t"
    D = round(1*p1+4*p2+9*p3+16*p4+25*p5 - M**2,3)
    answer += "D(X) = "+str(D)+"\t"
    Q = round(sqrt(D),3)
    answer+="Q(X) = "+str(Q)+"\n"
    F ="\t__________\n"
    F+="\t| 0\t, x<=1\n"
    F+="\t| "+str(round(p1,1))+"\t, 1<x<=2\n"
    F+="F(X) =\t| "+str(round(p1+p2, 2))+"\t, 2<x<=3\n"
    F+="\t| "+str(round(p1+p2+p3, 3))+" , 3<x<=4\n"
    F+="\t| "+str(round(p1+p2+p3+p4, 4))+", 4<x<=5\n"
    F+="\t| 1\t, 5<x\n"
    F+="\t‾‾‾‾‾‾‾‾‾‾"
    answer+=F
    task_and_answer=[task,answer]
    return task_and_answer

def task_12():
    task = "Задача №12\n"
    
    n = 3
    p = randint(1,9)/10
    q = round(1 - p,1)

    task += "Производится три независимых опыта, в каждом из которых событие появляется с вероятностью "+str(p)+" . Составить"
    task += "ряд распределения числа появлений события в трех опытах. Найти M(X) и D(X) этой случайной величины."
    
    answer = ""
    
    p0 = round(q * q * q, 3)
    p1 = round(3 * p * q * q, 3)
    p2 = round(3 * p * p * q, 3)
    p3 = round(p * p * p, 3)
    

    print()
    answer = "Ряд распределения: \nxi\t0\t1\t2\t3\n"
    answer += "pi\t"+str(p0)+"\t"+str(p1)+"\t"+str(p2)+"\t"+str(p3)+"\n\n"
    M = round(n*p,1)
    answer += "M(X) = "+str(M)+"\t"
    D = round(n*p*q,2)
    answer += "D(X) = "+str(D)+"\t"
    
    task_and_answer=[task,answer]
    return task_and_answer

def task_13():
    task = "Задача №13\n"
    r = randint(1,3)
    n=0
    if r==1:
        n = 1000
    elif r==2:
        n = 2000
    else:
        n = 10000
  
    p = 1/n

    task += "Устройство содержит "+str(n)+" одинаково надежных элементов, вероятность отказа каждого из них равна "
    task += str(p)+". Составить ряд распределения числа отказавших элементов. Найти M(X) этой случайной величины."
    
    answer = ""
    
    answer = "Ряд распределения: \nxi\t0\t1\t\t2\t\t\t...\tk\t\t\t...\tn\n"
    answer += "pi\te^(-λ)\tλ*e^(-λ)\t((λ^2)/2)*e^(-λ)\t...\t((λ^k)/k)*e^(-λ)\t...\t((λ^n)/n)*e^(-λ)\n\n"
    answer += ",где n = "+str(n)+"\tp = "+str(p)+"\tλ = n * p = "+str(n*p)+"\n\n"
    M = n*p
    answer += "M(X) = n * p = "+str(M)+"\t"
    
    task_and_answer=[task,answer]
    return task_and_answer

def task_14():#недоделано
    task = "Задача №14\n"
    
    F ="\t__________\n"
    F+="\t| 0\t\t, x<=1\t\tα = 1,2\n"
    F+="F(X) =\t| (x^2-x)/2\t, 1<x<=2\tβ = 1,5\n"
    F+="\t| 1\t\t, 2<x\n"
    F+="\t‾‾‾‾‾‾‾‾‾‾"
    a = 1.2
    b = 1.5
    

    task += "Дана функция распределения F(x) непрерывной случайной величины X.\nТребуется:\n"
    task += "\t1) найти плотность вероятности f(x);\n"
    task += "\t2) построить графики F(x) и f(x);\n"
    task += "\t3) найти M(X), D(X), (Х);\n"
    task += "\t4) найти Р(α < X < β) для данных α, β.\n"
    task += F
    print(task)
    answer = ""
    
    answer = "Ряд распределения: \nxi\t0\t1\t\t2\t\t\t...\tk\t\t\t...\tn\n"
    answer += "pi\te^(-λ)\tλ*e^(-λ)\t((λ^2)/2)*e^(-λ)\t...\t((λ^k)/k)*e^(-λ)\t...\t((λ^n)/n)*e^(-λ)\n\n"
    answer += ",где n = "+str(n)+"\tp = "+str(p)+"\tλ = n * p = "+str(n*p)+"\n\n"
    M = n*p
    answer += "M(X) = n * p = "+str(M)+"\t"
    
    task_and_answer=[task,answer]
    return task_and_answer

#print(task_14()[0])
#print(task_14()[1])
