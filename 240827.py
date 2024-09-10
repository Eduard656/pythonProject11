set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a.difference(set_b))
print(set_b.difference(set_a))

names = ['Jack','Mary','Samantha','George','Simon','John']
names_str = '\n'.join(names)
print(names_str)


numbers = [2, 53, 12, 87, 65, 32, 12, 2, 65, 32]
print(sum(numbers))
print(sum(set(numbers)))

numbersA = (23, 52, 12, 75, 42)
numbersB = (75, 22, 42, 94, 70)

print(set(numbersA).intersection(set(numbersB)))


a = (1, 2, 3, 4, 6, 7, 8)
a = list(a)
a.insert(4,5)
a= tuple(a)
print(a)