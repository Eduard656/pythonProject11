# empty = {}
# empty = dict()
# print(type(empty))


x = 5
sample = {
    'name':'Jack',
    'courses': ['Art','English','Programming'],
    1: 'int key',
    0.2:'float key',
    x: 'variable key',
    'dictionary': {'name': 'Bob','surname': 'Smith'}
}
#print(sample['name'])
#print(sample.get('hcdvhyv', {}))

# sample['name'] = 'Sarah'
# sample['phone'] = '555-555-5555'
# print(sample)
#
# sample.update({'name':'Bob','address': 'Tallinn'})
# print(sample)
#
# del sample['name']
# print(sample)
#
# courses = sample.pop('courses')
# print(courses)

# sample2 = {'name': 'Jack', "surname": 'Smith', 'age': 40}
# for x in sample2:
#     print(sample2[x])
#
# print(sample2.keys())
# print(sample2.values())
# print(sample2.items())
#
# for key, value in sample2.items():
#     print(key, value)

def say_hello(name, surname):
    return f'Hello {name} {surname}!'


#say_hello('Roman', 'Kutselepa')
x = say_hello('Roman', 'Kutselepa ')
print(x)

def short_or_long(string):
    if len(string) > 5:
        return 'long'
    else:
        return 'short'
    print('Goodbye')

print(short_or_long('Interstellar'))

words = ['Sun', 'Too','People','Paul']
for word in words:
    print(short_or_long(word))

def fizz_buzz(start, end):
    for num in range(start, end + 1):
        if num %3 == 0 and num % 5 == 0:
            print(num, 'FIZZBUZZ')
        elif num % 5 == 0:
            print(num, 'FIZZ')
        elif num % 3 == 0:
            print(num,'BUZZ')


# a = 1
# b = 2
# c = 3
#
# def sample():
#     global a, b
#     a =10
#     b = 20
#     c = 30
#     print(a, b, c)

# sample()
# print(a, b, c)



def triangle_area(a, b, c):
    p =(a + b + c) / 2
    area = (p *(p-a) * (p-b) * (p-c) ) ** 0.5
    return area

# print(triangle_area(3, 4, 5))

def print_result():
    print(f'The area of triaqngle is {triangle_area(3, 4, 5)} cm2')


print_result()