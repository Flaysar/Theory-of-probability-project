from random import randint
from random import uniform
import docx
import codecs
# inuform(начало, конец) - возрщает рандомное вещественное в диапазоне включая концы
# randint(начало, конец) - возрщает рандомное целое в диапазоне включая концы

from functions import local_lapl
from functions import integr_lapl
import Egors_tasks
import Magas_tasks
import Dima_tasks

N = 20  # сколько всего задач в варианте, исправить если что
tasks_num_list = set()  # множество заданий, которые нужно сгенерировать
select = input('Введите номера заданий (all для выбора всех) ')
if select == 'all':
    for i in range(1, N + 1):
        tasks_num_list.append(i)  # запишем все номеры
else:
    tasks_num_list = select.split(' ')  # это даст список из char символов строки, которые разделены пробелом
    tasks_num_list = [int(i) for i in tasks_num_list]  # переделает все char значения в списке в int-вые

variants_count = int(input('введите количество вариантов '))  # количество вариантов
tasks = open('задания.doc', 'w')
answers = open('ответы.doc', 'w')
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
