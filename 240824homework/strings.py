string1 = "Hello bro"
print(string1[:2]+string1[7:])

example_string2 = "jack Is My NAME"
print(example_string2.capitalize())

example_string3 = "%-*Get rid of *junk* please*-L%*"
print(example_string3.replace('*','').strip('%-L'))

example_string4 = "hello my name is jack"
print(example_string4.capitalize().replace('jack','Jack'))

example_string5 = "Welcome to estonia. Estonia is awesome, isn't it? I moved to ESTONIA 5 years ago."
print(example_string5.lower().count('estonia'))

var1 = "jack"
var2 = "hello"
var3 = "MY NAME IS"
print(f" {var2.capitalize()}, {var3.lower()}, {var1.capitalize()}")


byte_string = b"\316\273"
print(byte_string.decode())
