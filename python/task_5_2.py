boys_file_write = open('task_5_2_boys_school_grade.csv','w')
girls_file_write = open('task_5_2_girls_school_grade.csv','w')
pupils_file_read = open('task_5_2_school_grade.txt','r')
i=1
current_file = boys_file_write

all_lines = pupils_file_read.readlines()

for line in all_lines: #Reading all lines from a text file
    if i==1:
        line=line.rstrip() #The rstrip statement removes the '\ n' character denoting the end of the line.
        if line == "c":
            current_file = boys_file_write
        else :
            current_file = girls_file_write #d
        current_file.write(line+';')
        i+=1
    elif i==2 or i==3:
        line=line.rstrip()
        current_file.write(line+';')
        i+=1
    elif i==4:
        line=line.rstrip()
        current_file.write(line+'\n')
        i=1
              
boys_file_write.close()        
girls_file_write.close()
pupils_file_read.close()
