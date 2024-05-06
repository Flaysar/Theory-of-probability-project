from random import randint
from random import uniform
# inuform(начало, конец) - возрщает рандомное вещественное в диапазоне включая концы
# randint(начало, конец) - возрщает рандомное целое в диапазоне включая концы

from functions import local_lapl
from functions import integr_lapl
import Egors_tasks
import Magas_tasks
import Dima_tasks

from tkinter import *
from tkinter.ttk import Checkbutton


def clicked():
    global variants_count
    global tasks_num_list
    if txt.get() != '':
        variants_count = int(txt.get())
    else:
        variants_count = 1
    if chk_all.get():
        for i in range(1, 21):
            tasks_num_list.append(i)
    else:
        number = 1
        for i in check_list:
            if i.get():
                tasks_num_list.append(number)
            number += 1


variants_count = 0
tasks_num_list = []  # множество заданий, которые нужно сгенерировать

window = Tk()
window.geometry('400x300')

window.title('Окно выбора')
count_var_label = Label(window, text='Введите количество вариантов: ', )
count_var_label.grid(column=0, row=0)

txt = Entry(window, width=10)
txt.grid(column=1, row=0)
txt.focus()

tasks_label = Label(window, text='Выберите номера заданий:')
tasks_label.grid(column=0, row=1)

chk_all = BooleanVar()
chk_all.set(False)  # задайте проверку состояния чекбокса
all_tasks_check = Checkbutton(window, text='Все задания', var=chk_all)
all_tasks_check.grid(column=0, row=2)

check_list = []
for i in range(0, 20):
    check_list.append(BooleanVar())
    check_list[i].set(False)

for i in range(0, 20):
    if i < 9:
        task_check = Checkbutton(window, text=f'0{i + 1}', var=check_list[i])
    else:
        task_check = Checkbutton(window, text=f'{i + 1}', var=check_list[i])
    if i < 7:
        task_check.grid(column=0, row=i + 3)
    elif i < 14:
        task_check.grid(column=1, row=i % 7 + 3, ipadx=30, pady=0)
    else:
        task_check.grid(column=2, row=i % 14 + 3, ipadx=10, pady=0)

btn = Button(window, text='Создать документ', bg='green', fg='white', command=clicked)
btn.grid(column=0, row=15)

window.mainloop()

N = 20  # сколько всего задач в варианте

tasks = open('задания.doc', 'w', encoding='utf-8')
answers = open('ответы.doc', 'w', encoding='utf-8')
for i in range(0, variants_count):
    tasks.write(f'ВАРИАНТ {i + 1}\n')
    answers.write(f'ВАРИАНТ {i + 1}\n')
    for task in tasks_num_list:  # идем по списку с номерами заданий
        if task == 1:  # если номер = 1, то пишем его
            coin_flip = randint(1, 3)  # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:  # задание Егора
                text, answer = Egors_tasks.task_1()

            elif coin_flip == 2:
                text, answer = Magas_tasks.task_1()
            else:
                text, answer = Dima_tasks.task_1()
            tasks.write(text)
            answers.write(answer)
            continue

        if task == 2:  # если номер = 2, то пишем 2 и т.д.
            coin_flip = randint(1, 3)  # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:  # задание Егора
                text, answer = Egors_tasks.task_2()

            elif coin_flip == 2:
                text, answer = Magas_tasks.task_2()
            else:
                text, answer = Dima_tasks.task_2()
            tasks.write(text)
            answers.write(answer)
            continue

        if task == 3:
            coin_flip = randint(1, 3)  # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:  # задание Егора
                text, answer = Egors_tasks.task_3()

            elif coin_flip == 2:
                text, answer = Magas_tasks.task_3()
            else:
                text, answer = Dima_tasks.task_3()
            tasks.write(text)
            answers.write(answer)
            continue

        if task == 4:
            coin_flip = randint(1, 3)  # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:  # задание Егора
                text, answer = Egors_tasks.task_4()

            elif coin_flip == 2:
                text, answer = Magas_tasks.task_4()
            else:
                text, answer = Dima_tasks.task_4()
            tasks.write(text)
            answers.write(answer)
            continue

        if task == 5:
            coin_flip = randint(1, 3)  # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:  # задание Егора
                text, answer = Egors_tasks.task_5()

            elif coin_flip == 2:
                text, answer = Magas_tasks.task_5()
            else:
                text, answer = Dima_tasks.task_5()
            tasks.write(text)
            answers.write(answer)
            continue

        if task == 6:
            coin_flip = randint(1, 3)  # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:  # задание Егора
                text, answer = Egors_tasks.task_6()

            elif coin_flip == 2:
                text, answer = Magas_tasks.task_6()
            else:
                text, answer = Dima_tasks.task_6()
            tasks.write(text)
            answers.write(answer)
            continue

        if task == 7:
            coin_flip = randint(1, 3)  # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:  # задание Егора
                text, answer = Egors_tasks.task_7()

            elif coin_flip == 2:
                text, answer = Magas_tasks.task_7()
            else:
                text, answer = Dima_tasks.task_7()
            tasks.write(text)
            answers.write(answer)
            continue

        if task == 8:
            coin_flip = randint(1, 3)  # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:  # задание Егора
                text, answer = Egors_tasks.task_8()

            elif coin_flip == 2:
                text, answer = Magas_tasks.task_8()
            else:
                text, answer = Dima_tasks.task_8()
            tasks.write(text)
            answers.write(answer)
            continue

        if task == 9:
            coin_flip = randint(1, 3)  # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:  # задание Егора
                text, answer = Egors_tasks.task_9()

            elif coin_flip == 2:
                text, answer = Magas_tasks.task_9()
            else:
                text, answer = Dima_tasks.task_9()
            tasks.write(text)
            answers.write(answer)
            continue

        if task == 10:
            coin_flip = randint(1, 3)  # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:  # задание Егора
                text, answer = Egors_tasks.task_10()

            elif coin_flip == 2:
                text, answer = Magas_tasks.task_10()
            else:
                text, answer = Dima_tasks.task_10()
            tasks.write(text)
            answers.write(answer)
            continue

        if task == 11:
            coin_flip = randint(1, 3)  # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:  # задание Егора
                text, answer = Egors_tasks.task_11()

            elif coin_flip == 2:
                text, answer = Magas_tasks.task_11()
            else:
                text, answer = Dima_tasks.task_11()
            tasks.write(text)
            answers.write(answer)
            continue

        if task == 12:
            coin_flip = randint(1, 3)  # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:  # задание Егора
                text, answer = Egors_tasks.task_12()

            elif coin_flip == 2:
                text, answer = Magas_tasks.task_12()
            else:
                text, answer = Dima_tasks.task_12()
            tasks.write(text)
            answers.write(answer)
            continue

        if task == 13:
            coin_flip = randint(1, 3)  # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:  # задание Егора
                text, answer = Egors_tasks.task_13()

            elif coin_flip == 2:
                text, answer = Magas_tasks.task_13()
            else:
                text, answer = Dima_tasks.task_13()
            tasks.write(text)
            answers.write(answer)
            continue

        if task == 14:
            coin_flip = randint(1, 3)  # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:  # задание Егора
                text, answer = Egors_tasks.task_14()

            elif coin_flip == 2:
                text, answer = Magas_tasks.task_14()
            else:
                text, answer = Dima_tasks.task_14()
            tasks.write(text)
            answers.write(answer)
            continue

        if task == 15:
            coin_flip = randint(1, 3)  # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:  # задание Егора
                text, answer = Egors_tasks.task_15()

            elif coin_flip == 2:
                text, answer = Magas_tasks.task_15()
            else:
                text, answer = Dima_tasks.task_15()
            tasks.write(text)
            answers.write(answer)
            continue

        if task == 16:
            coin_flip = randint(1, 3)  # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:  # задание Егора
                text, answer = Egors_tasks.task_16()

            elif coin_flip == 2:
                text, answer = Magas_tasks.task_16()
            else:
                text, answer = Dima_tasks.task_16()
            tasks.write(text)
            answers.write(answer)
            continue

        if task == 17:
            coin_flip = randint(1, 3)  # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:  # задание Егора
                text, answer = Egors_tasks.task_17()

            elif coin_flip == 2:
                text, answer = Magas_tasks.task_17()
            else:
                text, answer = Dima_tasks.task_17()
            tasks.write(text)
            answers.write(answer)
            continue

        if task == 18:
            coin_flip = randint(1, 3)  # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:  # задание Егора
                text, answer = Egors_tasks.task_18()

            elif coin_flip == 2:
                text, answer = Magas_tasks.task_18()
            else:
                text, answer = Dima_tasks.task_18()
            tasks.write(text)
            answers.write(answer)
            continue

        if task == 19:
            coin_flip = randint(1, 3)  # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:  # задание Егора
                text, answer = Egors_tasks.task_19()

            elif coin_flip == 2:
                text, answer = Magas_tasks.task_19()
            else:
                text, answer = Dima_tasks.task_19()
            tasks.write(text)
            answers.write(answer)
            continue

        if task == 20:
            coin_flip = randint(1, 3)  # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:  # задание Егора
                text, answer = Egors_tasks.task_20()

            elif coin_flip == 2:
                text, answer = Magas_tasks.task_20()
            else:
                text, answer = Dima_tasks.task_20()
            tasks.write(text)
            answers.write(answer)
            continue

    tasks.write('\n\n')
    answers.write('\n\n')

    # if task == 21:
    #     coin_flip =  randint(1, 3) # 1 - вариант Егора, 2 - Маги, 3 - Димы
    #     if coin_flip == 1:
    #         pass # pass означает пропуск условия
    #         # задание Егора
    #     elif coin_flip == 2:
    #         pass
    #         # задание Маги
    #     else:
    #         pass
    #         # задание Димы
    #     tasks.write(text)
    #     continue
    #
    # if task == 22:
    #     coin_flip =  randint(1, 3) # 1 - вариант Егора, 2 - Маги, 3 - Димы
    #     if coin_flip == 1:
    #         pass # pass означает пропуск условия
    #         # задание Егора
    #     elif coin_flip == 2:
    #         pass
    #         # задание Маги
    #     else:
    #         pass
    #         # задание Димы
    #     tasks.write(text)
    #     continue

tasks.close()
answers.close()
