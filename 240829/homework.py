# Для диапозона чисел от 1 до 100 включительно
# Если число делится на 3 без остатка, вывести число и FIZZ
# Если число делится на 5 без остатка, вывести число и BUZZ
# Если число делится на 3 и на 5 без остатка, вывести число и FIZZBUZZ
# Каждое число выводится не больше одного раза

numbers = range(1,101)
for num in numbers:
    if num % 3 == 0 and num % 5 == 0:
        print(num ,'FIZZBUZZ')
    elif num % 3 == 0:
        print(num ,'FIZZ')
    elif num % 5 == 0:
        print(num ,'BUZZ')
