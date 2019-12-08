import random

fileWriter = open('wylosowane.txt','w')

a = int(input('Podaj max zakres liczb z których będą losowane liczby\n'))
b = int(input('Ile liczb chcesz wylosować?\n'))
i=0

for liczb in range(b):
    fileWriter.write(str(random.randrange(1,a+1)) + '\n')
    i+=1

print('Program wylosował '+str(i)+' liczb w zakresie od 1 do '+str(a)+', które zostały one zapisane w pliku wylosowane.txt')

fileWriter.close()
