import re

word = input("Enter word: ")

count = 0
countAdd = 1
output = ''
table = []
expression = '\''
table.append(word)
for check in word:
    for letter in word:
        count+=1
        if(count == countAdd):
            letter = '.'
        output += letter
    table.append(output)
    output = ''
    count = 0
    countAdd+=1
file_read = open('task_4_3_poem.txt','r')
i = 0
for expre in table:
    i+=1
    if(1-len(table) == 1-i):
        expression+=expre
    else:
        expression+=expre + '|'
expression+= '\''

print(expression)

p = re.compile(expression)
for line in file_read:
    if p.findall(line):
        print(" found")
    else:
        print(" not found")

file_read.close()
