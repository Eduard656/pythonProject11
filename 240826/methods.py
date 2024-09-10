# emty=[] # list()
#
# print(type(empty)) # list()
# print(bool(emty)) # empty list give false value

# filled = [123, 0.123, 'Hello', x, [1,2,[3,4,5],6], True, True, True]
# print(len(filled))
# print(filld[4][2][1])

courses = ['History','Math','Litreture','Physics','Programming']
# print(courses[1:4])
# print(courses[::-2])

# courses[0] ='Art'
# print(courses)

# courses.append('Art') NO print
# courses.insert(0, 'English')
# print(courses)
# courses.extend(['Art','Economics'])
# print(courses)

# courses.remove('Math')
# print(courses)
# print(courses.pop(0))
# print(courses)

# courses.reverse() no orig

# courses.sort(reverse=True)
# print(courses)

# print(min(courses))
# print(max(courses))
# print(min('Hello world'))
# print(max('Hello world'))
# print(sum[123 , 456 , 3 , 45])

print('Math' in courses)
print('world' in 'Hello world')

print('Hello people of planet earth'.split())

# user_input=input('Enter something: ')
# print(user_input.split(','))            STR

print('-'.join(courses))

a='one'
b=a
a+='two'
print(a, b)

# a=[1, 2, 3, 4, 5]
# b=a.copy()      without copy a,b the same
# a.append(555)
# b.append(777)
# print(a)
# print(b)

# emty =()
# emty = tuple()
# print(type(emty))

x=set()
print(type(x))

courses = {'History','Math','Math','Litreture','Physics','Programming'}
courses2 = {'Math','Economics', 'History','Spanish'}
print(courses.difference(courses2))
print(courses2.difference(courses))
print(courses.intersection(courses2))
