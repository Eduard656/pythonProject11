age = 20
if age > 0:
    if age <= 10:
        print('He is a child.')
    elif age < 18:
        print('He is a teenager')
    else:
        print('He is adult.')
else:
    print('Check your age!')

# username = input('Enter your username:')
# if username:
#     print(f'Hello {username}')
# else:
#     print('Hello stranger')

# idcode = '38803160272'
# if idcode.isdecimal():
#     if len(idcode) != 11:
#         if len(idcode) < 11:
#             print('ID you entered is too short!')
#         else:
#             print('ID you entered is too long')
#     else:
#         print('ID not correct.')
#
# else:
#     print('ID you entered is not numeric!')

# x = True
# x and print('Hello world')

age = 20

# if age <= 10 and age>0:
#     print('He is a child.')
# if age < 18 and age >10:
#     print('He is a teenager')
# if age >=18:
#     print('He is adult.')

# names = {'Jack','Samatha','Bob','John'}
# for name in names:
#     print(f'Hello {name}')

# people = [
#     ['Jack', 34, 'm'],
#     ['Samatha', 28,'f'],
#     ['Sarah', 27, 'f'],
#     ['Bob', 16,'m'],
#     ['Simon', 42,'m']
# ]
# for person in people:
#     if person[2] == 'm':
#         print(f'This is {person[0]}. He is {person[1]} years old')
#     elif person[2] == 'f':
#         print(f'This is {person[0]}. She is {person[1]} years old')

# for name, age, gender in people:
#      if gender == 'm':
#          print(f'This is {name}. He is {age} years old')
#      elif gender == 'f':
#          print(f'This is {name}. She is {age} years old')


# for num1 in range(10):
#     for num2 in range(10):
#         for num3 in range(10):
#             for num4 in range(10):
#                 print(num1, num2, num3, num4)

# counter = 0
# while counter < 10:
#     print(counter)
#     counter += 1

# while True:
#      idcode = input('Please enter your national id: ')
#      if idcode.isdecimal():
#          if len(idcode) != 11:
#              if len(idcode) < 11:
#                  print('ID you entered is too short.')
#                  continue
#              else:
#                  print('ID you entered is too long.')
#                  continue
#          else:
#              while True:
#                  name= input('Enter name: ')
#              if not name:
#                 print('Try again!')
#                 continue
#          # exit()
#          # quit()
#          break
#      else:
#          print('ID you entered is not numeric!')
#          continue
# print('Good bye!')


# try:
#     # int('123')
#     # 5 / 0
#     name= input('Enter name: ')
#     if not name:
#         raise Exception
# except ValueError:
#     print(('ERROR'))
# exept ZeroDivisionError:
#     print('Dont divide by 0')
# exept Exception:
#     print('Name is empty')
# else:
#     print('NO ERROR')
# finally:
#     print('Good bye!')



