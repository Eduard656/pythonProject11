# Write a program that converts given string to datetime object
#import datetime

import datetime

sample1 = 'Jan 1 2014 2:43PM'
sp = datetime.datetime.strptime(sample1, '%b %d %Y %I:%M%p')
print(sp)

sample2 = '14:20 10/12/22'
sp2 = datetime.datetime.strptime(sample2, '%H:%M %y/%m/%d')
print(sp2)

sample3 = 'Tuesday, September 24, 2019'
sp3 = datetime.datetime.strptime(sample3, '%A, %B %d, %Y')
print(sp3)

sample4 = '01.01.1970 - 00:00:01'
sp4 = datetime.datetime.strptime(sample4, '%d.%m.%Y - %H:%M:%S')
print(sp4)

# Write a program to print yesterdays, today and tomorrow dates
tdelta = datetime.timedelta(hours=24)
a = datetime.date.today()
b = a - tdelta
c = a + tdelta
print(b , a , c)

#Write a program to convert given timestamp to dd.mm.yyyy format
some_day = 1014163200
ndatetime = datetime.datetime.fromtimestamp(some_day)
print(ndatetime.strftime('%d.%m.%Y'))

# Write a function to subtract 2 weeks from timestamp and return new timestamp


# def get ts2():
#   ts2 = ((ts/1000000) - 14*24*60*600) * 1000000
#   print(ts2)

#input: timestamp (float)
# output: timestamp (float)

