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
  text = ''
  rand_condition = randint(1, 3) # пусть это разные условия для одной задачи
  if rand_condition == 1:
    my_rand = randint(1, 2) # это разные формулировки одной задачи
    if my_rand == 1:
      text+='не содержит четных цифр '
    else:
      text+='все числа нечетны '

  elif rand_condition == 2:
      my_rand = randint(1, 2)
      if my_rand == 1:
        text+='не содержит нечетных цифр '
      else:
        text+='все числа четны '
  else:
      rand1 = randint(0, 9)
      rand2 = randint(0, 9)
      while(rand1==rand2): rand2 = randint(0, 9)
      text+=f'не содержит цифры {rand1} и {rand2} ' # с помощью f' {какая-то переменная}' можно вставлять переменные в строки
  return text

