fileWrite = open('dane.csv','w')
fileRead = open('dane.txt','r')
i=1

all_lines = fileRead.readlines()

#Reading all lines from a text file
for line in all_lines:
    if (i==1):
        #The rstrip statement removes the '\ n' character denoting the end of the line.
        line=line.rstrip()
        fileWrite.write(line+';')
        i+=1
    elif (i==2):
        line=line.rstrip()
        fileWrite.write(line+';')
        i+=1
    elif (i==3):
        fileWrite.write(line)
        i=1
fileWrite.close()
fileRead.close()
