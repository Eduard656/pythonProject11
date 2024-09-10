from enum import unique

with open('trimushketera.txt', 'r', encoding='UTF8') as file:
#data = file.read()
#data = data.lower()
    file_content = file.read().lower()
    file_content = file_content.replace(' ','')
    file_content = file_content.replace('.','')
    file_content = file_content.replace(',','')
    file_content = file_content.replace('!','')
    file_content = file_content.replace('?','')
    file_content = file_content.replace(':','')
    file_content = file_content.replace(';','')
    file_content = file_content.replace('(','')
    file_content = file_content.replace(')','')
    file_content = file_content.replace('*','')
data = file_content.count('')
#print(file_content.count(''))
with open(r'homeworkcopy.txt', 'w', encoding='UTF8') as file2:
    file2.write(str(data))
    words = data.split()
    unique = list(set(words))
    unique.sort()