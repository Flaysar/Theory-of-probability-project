import math
# Здесь будут функции для сочетаний и т.д, функции для таблиц Лапласа и для нахождения мат.ожидания и т.д.

# Перестановка
def transposition(num):  
  return f'{num}!', math.factorial(num)

# Перестановка с повторением
def transposition_with_repeat(*nums):
  cross_fact = 1
  all_fact = 0
  text = ''
  for i in nums:
      cross_fact*=math.factorial(i)
      text+=f'{i}!*'
      all_fact+=i
  return str(all_fact)+'!/'+text[:-1], math.factorial(all_fact)/cross_fact  

# Cочетание
def combination(n, k):
   return f'{n}!/({n-k}!*{k}!)', math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

# Сочетание с повторением
def combination_with_repeat(n, k):
   return f'{n+k-1}!/({n-1}!*{k}!)', math.factorial(n+k-1)/(math.factorial(n-1)*math.factorial(k))

# Размещение
def placement(n, k):
   return f'{n}!/{n-k}!', math.factorial(n)/math.factorial(n-k)

# Размещение с повторением
def placement_with_repeat(n, k):
   return f'{n}^{k}', n**k


#Локальная и интегральная таблицы Лапласа

# Здесь работаю с файлами, в которых лежат табличные значения
local_teor_file = open('local_teor.txt', 'r')
local_teor_list = []
for line in local_teor_file:
  line = line[:-1]
  my_list = line.split(' ')
  local_teor_list.append(my_list[1:])

integr_teor_file = open('integr_teor.txt', 'r')
integr_teor_dict = {}
counter = 0
for line in integr_teor_file:
  line = line[:-1]
  my_list = line.split('\t')
  my_list = [float(i) for i in my_list]
  integr_teor_dict[my_list[0]]=my_list[1]
  
# Локальная
def local_lapl(num):
    num = abs(num)
    if num>=4:
      return 0
    m1 = int(num*100//10)
    m2 = int(num*100%10)
    return local_teor_list[m1][m2]

# Интегральная
def integr_lapl(num):
  if 3.61<num<3.89:
     return 0.4999
  elif num>3.89:
      return 0.5
  elif -3.61>num>-3.89:
     return -0.4999
  elif num<-3.89:
      return -0.5
  elif num<0:
      return -integr_teor_dict[-num]
  else: return integr_teor_dict[num]


# Для дискретных случайных величин
# Диск. Мат ожидание
def discr_math_expectation(my_dict):
   sum=0
   for x, p in my_dict.items():
      sum+=x*p
   return round(sum, 3)

# Дискр. Дисперсия
def discr_dispersion(my_dict):
   sec_dict = {}
   for x, p in my_dict.items():
      sec_dict[x**2]=p
   math_squares = discr_math_expectation(sec_dict)
   return round(math_squares - discr_math_expectation(my_dict)**2, 3)

# Дискр. Среднеквадратичное отклонение
def discr_standart_deviation(my_dict):
   return round(math.sqrt(discr_dispersion(my_dict)), 3)

# Для непрерывных случайных величин
