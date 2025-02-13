import os
'''
Here we are opeing the file we will be first looking at.
This we be our testing file and thus the goal will be simple,
to tokeniz and keep track of each word that appers

So ideally we will have the white space or ' ' be the trigger
to start a new word entry in the dictionary

This lab will be two parts:
One: The reading and coverting of the text file into a dictionary
and 
Second: The writing of the dictionary to a diffrent txt file
'''

#First we open the file we want, and for now we will hard code the txt file
#It will be saved as fd
fd = os.open("speech.txt", os.O_RDONLY)

'''
For a lil funny idea what we could have done is a sliding window
we set it to increment with the catch and rest condition being that of the white
space
'''
cleverName = os.read(fd, 10)

for i in cleverName:
        print(i)
