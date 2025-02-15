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
currentFile = os.open("speech.txt", os.O_RDONLY)

'''
So what we be doing here is having a small buffured reader that takes in a total of
100 bytes at a time.  Followed by that in the for loop we will decode the data
'''
cleverName = os.read(currentFile, 200)
currentWord = ''
dictionaryList = {}
for i in cleverName.decode():
        print(i)
        currentWord += i
        if(i==' ' or i == '\n') and currentWord[:-1] in dictionaryList:
                dictionaryList[currentWord[:-1]] += 1
                currentWord = ''
        elif(i==' ' or i == '\n') and not currentWord[:-1] in dictionaryList:
                dictionaryList[currentWord[:-1]] = 1
                currentWord = ''

        


print(dictionaryList)
                
        
