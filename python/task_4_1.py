"""
A text file is given - task_4_1_vulgar_text. Write a program that will rewrite all obscene words in Polish into a new file. Use regular expressions to catch as many profanity as possible (consider the word variation).
"""

import re
file_read=open('task_4_1_vulgar_text.txt','r')
file_write=open('task_4_1_indecent_words.txt','w')

p = re.compile("([^ ]*chuj[^ ]*)|([^ ]*jeb[^ ]*)|([^ ]*pier[^ ]*)|([^ ]*kurw[^ ]*)|([^ ]*piz[^ ]*)|([^ ]*skur[^ ]*)|([^ ]*dup[^ ]*)")

for line in file_read:
    words=line.split(" ")

    for word in words:
        if p.match(word):
            file_write.write(word)      
        
file_read.close()
file_write.close()
