#'r' - read
#'w' - write
#'a' - append
#'x' - create
#'r+' - read and write
#C:\Users\Home\PycharmProjects\pythonProject1\240906\files.py

#240906/files.py

# file = open(r'test.txt', 'r',encoding='cp1257')
#
# print(file.encoding)
# print(file.mode)
# print(file.closed)
# file.close()
# print(file.closed)

#with open(r'test.txt', 'r+',encoding='cp1257') as file:
#    # data = file.read()
#    # print(data)
#     data = file.readline()
#     print(data)
#     while len(data) >0:
#        data = file.readline()
#     #data2 = file.readline()
#     print(data)
#     data = file.read()
#     file.seek(0)
#     file.write(data.upper())
#
# data = data.lower()
# with open(r'text_files\test_copy.txt', 'w', encoding='utf8') as file2:
#     file2.write(data)

with open('pic1.jpg','rb') as file:
    data = file.read()
    with open('pic1_copy.jpg','wb') as file2:
        file2.write(data)

