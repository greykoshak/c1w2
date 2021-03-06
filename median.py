# Итак, мы с вами разобрали, как работают списки. Давайте попробуем решить задачу на их применение.
# В качестве примера попробуем найти медиану случайного списка. Медиана — это значение в отсортированном списке, которое
# лежит ровно посередине, таким образом, половина значений — слева от него, и половина значений — справа. Чтобы получить
# медиану случайного списка, нам нужно случайный список создать. Давайте воспользуемся для этого модулем random в
# стандартной библиотеке. Заведём наш список numbers. Давайте, у нас будет какое-то случайное количество элементов в
# этом списке, чтобы было интереснее. У нас будет number_size, который мы получим с помощью функции randint.
# Функция randint возвращает какое-то случайное значение в интервале, ей переданном. Таким образом, у нас number_size
# будет равняться от 10 до 15, какому-то числу. Теперь нам нужно создать наш случайный список. Давайте воспользуемся
# циклом for и встроенной функцией range. Будем интерироваться ровно number_size раз. Обратите внимание, я использую
# переменную нижнее подчёркивание, которая говорит о том, что нам не интересно, в принципе, что в неё записывается.
# Мы не будем её использовать. Нам важно, чтобы итерация происходила ровно number_size раз. И будем добавлять в наши
# numbers с помощью знакомого вам метода append какое-то новое число. А случайное число мы будем получать с помощью той
# же самой функции randint, и пусть это число будет от 10 до 20. Давайте выведем наш список. Отлично. У нас получился
# список со случайными значениями, они не отсортированы, и, как видно, от 11 до 20, насколько я вижу. Теперь, чтобы
# найти медиану, нам нужно список отсортировать. Давайте используем для этого встроенный в список метод sort и
# отсортируем его. sort сортирует in place, поэтому наш список уже должен быть отсортирован, давайте выведем его.
# Отлично, 11 в начале, 20 в конце, значит, список отсортирован. Теперь нам нужно взять какое-то среднее значение.
# Как вы могли догадаться, случая может быть два. Если у нас количество элементов в списке нечётное, то всё просто.
# Мы просто берём средний элемент. Если количество элементов чётное, то по определению медианы нам нужно взять среднее
# арифметическое от двух средних элементов. Давайте заведем переменную half_size, в которую положим значение, равное
# половине длины списка. Для этого используем встроенную функцию len и поделим нашу длину пополам. И заведём переменную
# медиана, которая будет для начала равняться None. Итак, в простейшем случае у нас нечётное количество элементов.
# Если у нас наш number_size нечётный, то есть при делении на два даёт остаток один, то мы просто берём в качестве
# медианы numbers(half_size). Однако интересное происходит, когда у нас чётное количество элементов в нашем списке.
# В таком случае нам нужно взять среднее из двух чисел, которые лежат посередине. Воспользуемся знакомой вам функцией
# sum встроенной и срезом. Нам нужен срез от half_size -1 до half_size +1. Обратите внимание, элементы нумеруются с
# нуля, поэтому именно так нам нужно поступать. И мы берём среднее арифметическое, поэтому делим на два. Давайте
# попробуем вывести нашу медиану. У нас получилось значение, и, на самом деле, это действительно медиана нашего списка.
# Чтобы это проверить, можно воспользоваться встроенным модулем statistics, который позволяет нам сделать то, что мы
# делали только что какое-то заметное количество времени, намного быстрее. Давайте импортируем модуль statistics, и у
# statistics есть метод median, который позволит нам найти медиану очень легко. Отлично. Медиана действительно равна 15.
# Мы с вами не только разобрали списки, но и посмотрели задачу на их применение.

import random

numbers = []
numbers_size = random.randint(10, 15)

for _ in range(numbers_size):
    numbers.append(random.randint(10, 20))

print(numbers)

numbers.sort()
print(numbers)

half_size = len(numbers) // 2
median = None

if numbers_size % 2 == 1:
    median = numbers[half_size]
else:
    median = sum(numbers[half_size-1:half_size+1]) / 2   # !Хозяйке на заметку: numbers[3:4] --> sum(numbers[3:4])

print(median)

# Проверка с помощью встроенной функции

import statistics

m = statistics.median(numbers)
print(m)