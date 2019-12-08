fileWrite = open('nowyTekst.txt','w')
fileRead = open('tekst.txt','r')

all_lines = fileRead.readlines()

#Reading all lines from a text file
for line in all_lines:
    #The rstrip statement removes the '\ n' character denoting the end of the line.
    line=line.rstrip()
    fileWrite.write(line + line[-12:] +"\n")
fileWrite.close()
fileRead.close()
