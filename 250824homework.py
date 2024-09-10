current_year = 2023
year_of_birth = 1988
years = current_year - year_of_birth
code_1 = 354
code_3 =  132
x = 152
y = 132
code_2 = (round(( x % y * 13) ** 0.5))
user_name = "John"
user_surname = "Smith"
print( "Hello " +  user_name +" " +  user_surname + ". You are " + str(years) +
       " years old. Your secret code is " + str(code_1) +"-"+ str(code_2) +"-" + str(code_3) +".")