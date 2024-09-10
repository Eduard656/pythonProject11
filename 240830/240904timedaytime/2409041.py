import datetime

# d = datetime.date(2024, 9, 1)
# print(d.year)
# print(type(d))
# today = datetime.date.today()
#
# #
# diff = today - d
# print(diff)
# print(type(diff))
#
tdelta = datetime.timedelta(hours=18, minutes=33)
# print(today + tdelta)
# print(tdelta.total_seconds())

# t = datetime.time(12, 43, 17)
# print(t)
# print(type(t))

# dt = datetime.datetime(2024, 9, 4, 18, 30, 15)
# #
# today = datetime.datetime.today()
# print(today)

# today = datetime.datetime.today()
#
# print(today.strftime('%d %B %Y'))

today = datetime.datetime.today()
print(today.timestamp())
ts = 1725471972.776895
new_datetime = datetime.datetime.fromtimestamp(ts)
print(new_datetime)

