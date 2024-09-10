# Написать программу, запрашивающую имя, фамилию и возраст пользователя и выводящую строку вида:
#         Hello, <Фамилия пользователя> <Имя пользователя>. Your age is: <возраст>

# a = input('Please enter you surname and name:')
# b = input('Please enter your age:')
# print(('Hello, ' + a),('.Your age is:' + b ))

# 2 Напишите программу, которая находит длину гипотенузы для прямоугольного треугольника по двум катетам. (
#     с = sqrt(a * a  +  b * b))

# a = input(' a:')
# b = input(' b:')
# a = int(a)
# b = int(b)
# c = (a * a + b * b) ** 0.5
#print(c)

# Пользователь вводит длины трех сторон треугольника (a,b,c) [тип float].
# Напишите программу, которая проверяет, является ли треугольник прямоугольным (с**2=a**2+b**2) 3, 4, 5

# a = input('a: ')
# b = input('b: ')
# c = input('c: ')
# a = int(a)
# b = int(b)
# c = int(c)
# if c**2 == a**2 + b**2:
#     print('True')

# Пользователь вводит некоторый произвольный список list.
# Написать программу, выводящую элементы списка в обратном порядке.

# mylist = input('Enter'Mama','Papa','Baba','Deda')
#for item in user_list[::-1]
# print(item)


# Как известно, кортеж является неизменяемым типом. Напишите программу, которая позволяет в кортеж A добавить кортеж B таким образом, что кортеж B помещается на index[2].
#         Пример: (1, 2, 3, 5, 8) (8,2,5) → (1, 2, 8, 2, 5, 3, 5, 8)

#
# test_list = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6]
# max_count = 0
# result = []
#
# for number in test_lst:
#     if test+lst.count(number) > max_count:
#         max_count = test_list.count(number)
#
# for number in test_list:
#     if test_lst.count(number) ==max_count:
#         if number not in result:
#             result.append(number)

seconds = 1234565

days = seconds // (24 * 60 * 60)
seconds %= (24 * 68 *60)
hours = seconds // (60*60)
seconds %= (60*60)
minutes = seconds // 60
seconds %= 60

print(f'{days}:{hours}:{minutes}:{seconds}')



