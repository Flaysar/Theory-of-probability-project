from random import randint
from random import uniform
import docx
import codecs
#inuform(начало, конец) - возрщает рандомное вещественное в диапазоне включая концы
#randint(начало, конец) - возрщает рандомное целое в диапазоне включая концы

from functions import local_lapl
from functions import integr_lapl
import Egors_tasks #так импортируется файл со своими функциями

N = 25 # сколько всего задач в варианте, исправить если что
tasks_num_list = set() # множество заданий, которые нужно сгенерировать
select = input('Введите номера заданий (all для выбора всех) ')
if select == 'all':
    for i in range(1, N+1):
        tasks_num_list.append(i) # запишем все номеры
else:
    tasks_num_list = select.split(' ') #это даст список из char символов строки, которые разделены пробелом
    tasks_num_list = [int(i) for i in tasks_num_list] # переделает все char значения в списке в int-вые

variants_count = int(input('введите количество вариантов ')) # количество вариантов
doc = docx.Document()
for i in range(0, variants_count):
    doc.add_paragraph(f'Вариант {i+1}')
    for task in tasks_num_list: # идем по списку с номерами заданий
        text = ''
        if task == 1: # если номер = 1, то пишем его
            coin_flip = randint(1, 3) # 1 - вариант Егора, 2 - Маги, 3 - Димы
            coin_flip = 1 #!!!!!!!!!!!!!! убрать потом
            if coin_flip == 1: # задание Егора
                text = '1. На штрафной стоянке наугад выбирают автомобиль с четырехзначным номером. Найти вероятность того, что его номер: \na) '
                text+=Egors_tasks.task_1()

            elif coin_flip == 2:
                pass # pass это пропуск if
                # задание Маги
            else:
                pass # pass это пропуск if
                # задание Димы
            doc.add_paragraph(text)
            continue

        if task == 2: # если номер = 2, то пишем 2 и т.д.
            coin_flip = randint(1, 3) # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:
                pass # pass означает пропуск условия
                # задание Егора
            elif coin_flip == 2:
                pass
                # задание Маги
            else:
                pass
                # задание Димы
            doc.add_paragraph(text)
            continue

        if task == 3:
            coin_flip = randint(1, 3) # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:
                pass # pass означает пропуск условия
                # задание Егора
            elif coin_flip == 2:
                pass
                # задание Маги
            else:
                pass
                # задание Димы
            doc.add_paragraph(text)
            continue

        if task == 4:
            coin_flip = randint(1, 3) # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:
                pass # pass означает пропуск условия
                # задание Егора
            elif coin_flip == 2:
                pass
                # задание Маги
            else:
                pass
                # задание Димы
            doc.add_paragraph(text)
            continue

        if task == 5:
            coin_flip = randint(1, 3) # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:
                pass # pass означает пропуск условия
                # задание Егора
            elif coin_flip == 2:
                pass
                # задание Маги
            else:
                pass
                # задание Димы
            doc.add_paragraph(text)
            continue

        if task == 6:
            coin_flip = randint(1, 3) # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:
                pass # pass означает пропуск условия
                # задание Егора
            elif coin_flip == 2:
                pass
                # задание Маги
            else:
                pass
                # задание Димы
            doc.add_paragraph(text)
            continue

        if task == 7:
            coin_flip = randint(1, 3) # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:
                pass # pass означает пропуск условия
                # задание Егора
            elif coin_flip == 2:
                pass
                # задание Маги
            else:
                pass
                # задание Димы
            doc.add_paragraph(text)
            continue

        if task == 8:
            coin_flip = randint(1, 3) # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:
                pass # pass означает пропуск условия
                # задание Егора
            elif coin_flip == 2:
                pass
                # задание Маги
            else:
                pass
                # задание Димы
            doc.add_paragraph(text)
            continue

        if task == 9:
            coin_flip = randint(1, 3) # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:
                pass # pass означает пропуск условия
                # задание Егора
            elif coin_flip == 2:
                pass
                # задание Маги
            else:
                pass
                # задание Димы
            doc.add_paragraph(text)
            continue

        if task == 10:
            coin_flip = randint(1, 3) # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:
                pass # pass означает пропуск условия
                # задание Егора
            elif coin_flip == 2:
                pass
                # задание Маги
            else:
                pass
                # задание Димы
            doc.add_paragraph(text)
            continue

        if task == 11:
            coin_flip = randint(1, 3) # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:
                pass # pass означает пропуск условия
                # задание Егора
            elif coin_flip == 2:
                pass
                # задание Маги
            else:
                pass
                # задание Димы
            doc.add_paragraph(text)
            continue


        if task == 12:
            coin_flip =  randint(1, 3) # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:
                pass # pass означает пропуск условия
                # задание Егора
            elif coin_flip == 2:
                pass
                # задание Маги
            else:
                pass
                # задание Димы
            doc.add_paragraph(text)
            continue

        if task == 13:
            coin_flip = randint(1, 3) # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:
                pass # pass означает пропуск условия
                # задание Егора
            elif coin_flip == 2:
                pass
                # задание Маги
            else:
                pass
                # задание Димы
            doc.add_paragraph(text)
            continue

        if task == 14:
            coin_flip = randint(1, 3) # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:
                pass # pass означает пропуск условия
                # задание Егора
            elif coin_flip == 2:
                pass
                # задание Маги
            else:
                pass
                # задание Димы
            doc.add_paragraph(text)
            continue

        if task == 15:
            coin_flip = randint(1, 3) # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:
                pass # pass означает пропуск условия
                # задание Егора
            elif coin_flip == 2:
                pass
                # задание Маги
            else:
                pass
                # задание Димы
            doc.add_paragraph(text)
            continue

        if task == 16:
            coin_flip =  randint(1, 3) # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:
                pass # pass означает пропуск условия
                # задание Егора
            elif coin_flip == 2:
                pass
                # задание Маги
            else:
                pass
                # задание Димы
            doc.add_paragraph(text)
            continue

        if task == 17:
            coin_flip =  randint(1, 3) # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:
                pass # pass означает пропуск условия
                # задание Егора
            elif coin_flip == 2:
                pass
                # задание Маги
            else:
                pass
                # задание Димы
            doc.add_paragraph(text)
            continue

        if task == 18:
            coin_flip =  randint(1, 3) # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:
                pass # pass означает пропуск условия
                # задание Егора
            elif coin_flip == 2:
                pass
                # задание Маги
            else:
                pass
                # задание Димы
            doc.add_paragraph(text)
            continue

        if task == 19:
            coin_flip =  randint(1, 3) # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:
                pass # pass означает пропуск условия
                # задание Егора
            elif coin_flip == 2:
                pass
                # задание Маги
            else:
                pass
                # задание Димы
            doc.add_paragraph(text)
            continue

        if task == 20:
            coin_flip =  randint(1, 3) # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:
                pass # pass означает пропуск условия
                # задание Егора
            elif coin_flip == 2:
                pass
                # задание Маги
            else:
                pass
                # задание Димы
            doc.add_paragraph(text)
            continue

        if task == 21:
            coin_flip =  randint(1, 3) # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:
                pass # pass означает пропуск условия
                # задание Егора
            elif coin_flip == 2:
                pass
                # задание Маги
            else:
                pass
                # задание Димы
            doc.add_paragraph(text)
            continue

        if task == 22:
            coin_flip =  randint(1, 3) # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:
                pass # pass означает пропуск условия
                # задание Егора
            elif coin_flip == 2:
                pass
                # задание Маги
            else:
                pass
                # задание Димы
            doc.add_paragraph(text)
            continue

        if task == 23:
            coin_flip =  randint(1, 3) # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:
                pass # pass означает пропуск условия
                # задание Егора
            elif coin_flip == 2:
                pass
                # задание Маги
            else:
                pass
                # задание Димы
            doc.add_paragraph(text)
            continue

        if task == 24:
            coin_flip =  randint(1, 3) # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:
                pass # pass означает пропуск условия
                # задание Егора
            elif coin_flip == 2:
                pass
                # задание Маги
            else:
                pass
                # задание Димы
            doc.add_paragraph(text)
            continue

        if task == 25:
            coin_flip =  randint(1, 3) # 1 - вариант Егора, 2 - Маги, 3 - Димы
            if coin_flip == 1:
                pass # pass означает пропуск условия
                # задание Егора
            elif coin_flip == 2:
                pass
                # задание Маги
            else:
                pass
                # задание Димы
            doc.add_paragraph(text)
            continue
    doc.add_paragraph('')
doc.save('вывод.docx')
