"""
Task: Write a random text generator. Acquire a collection of at least 100 words. Generate a random string of words from them (number of words given by the user).
"""

import random
how_many_words=int(input("Enter, how many words to generate : "))
word_list = ['a','about','all','also','and','as','at','be','because','but','by','can','come','could','day','do','even','find','first','for','from','get','give','go','have','he','her','here','him','his','how','I','if','in','into','it','its','just','know','like','look','make','man','many','me','more''my','new','no','not','now','of','on','one','only','or','other','our','out','people','say','see','she','so','some','take','tell','than','that','the','their','them','then','there','these','they','thing','think','this','those''time''to','two','up','use','very','want','way','we','well','what','when','which','who','will','with','would''year','you','your']
i=1
while i <= how_many_words:
    wordw_item = random.choice(word_list)
    print ("Randomly selected word from list is - ", wordw_item)
    i+=1
