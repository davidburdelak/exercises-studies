file_write = open('list_cen.txt','w')
file_read = open('list.txt','r')
i=1

all_lines = file_read.readlines()

for line in all_lines: #Reading all lines from a text file
    if (i==1):
        file_write.write(line)
        i+=1
    elif (i==2):
        file_write.write(line)
        i+=1
    elif (i==3):
        i+=1    
    elif (i==4):
        file_write.write(line)
        i+=1
    elif (i==5):
        file_write.write(line)
        i+=1
    elif (i==6):
        i+=1    
    elif (i==7):
        file_write.write(line)
        i+=1
    elif (i==8):
        file_write.write(line)
        i+=1
    elif (i==9):
        i+=1    
    elif (i==10):
        file_write.write(line)
        i+=1
    elif (i==11):
        file_write.write(line)
        i+=1
    elif (i==12):
        i+=1    
    elif (i==13):
        file_write.write(line)
        i+=1
    elif (i==14):
        file_write.write(line)
        i+=1     
    elif (i==15):
        i=1       
             
file_write.close()
file_read.close()

