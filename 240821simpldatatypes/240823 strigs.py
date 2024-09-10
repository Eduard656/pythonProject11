# """
# from html.parser import commentclose
#
# Block comment
# """
string_sample1 = " Hello world world"
german_sample = " der Fluß "
string_sample2 = "Kihhbybd hggTyfg"
string_sample3 = "  *   cannt understand      "
#
#
# print(string_sample1[-1])
# print(len(string_sample1))
# print(string_sample1[5:])
# print(string_sample1[:5])
# print(string_sample1[0:10:3])
# print(string_sample1[::2])
# print(string_sample1[::-1])

print(string_sample1.upper())
print("hello" == "Hello")
print("a" > "A")
print(german_sample.lower())
print(german_sample.casefold())

print(string_sample2.capitalize())
print(string_sample2.title())

print(string_sample1.istitle())
print(string_sample3.strip(" *"))

print(string_sample1.replace("world",  "planet", 1))
print(string_sample1.replace("world"," "))

print(string_sample1.count("o", 8))

print(string_sample1.find("world",8))

salary = 1000
string = 'Jons salary is {1}.{0}-{1}-{0}'
print(string.format(salary, True))
string = 'This {product} costs {price:.2f}.'
print(string.format(product='computer', price=1000))

name = 'jack'
surname = 'Smith'
salary = 1500

print(f'This is {name.title()} {surname}. His salary is {salary}')

# (byte_string.decode('utf-8'))

print(len('Thats\'s'))
print("My favorite book is \"Metro 2033\"")
print('\tHello\nworld')


