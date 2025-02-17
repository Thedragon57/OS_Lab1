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
print("Option 1 is the declartion.txt option 2 is the speech.txt")
while True:
        fileSelect = input()

        if fileSelect == "1":
                fileSelect = "declaration.txt"
                break
        elif fileSelect == "2":
                fileSelect = "speech.txt"
                break
        else: 
                print("Please chose options 1 or 2")

currentFile = os.open(fileSelect, os.O_RDONLY)

'''
So what we be doing here is having a small buffured reader that takes in a total of
100 bytes at a time.  Followed by that in the for loop we will decode the data
'''
cleverName = os.read(currentFile, 100)
currentWord = ''
dictionaryList = {}
while cleverName != b'':
        for i in cleverName.decode():
                print(i)
                currentWord += i
                if(i==' ' or i == '\n' or i == '.' or i == ',' or i == ';' or i == '"') and currentWord[:-1].lower() in dictionaryList:
                        dictionaryList[currentWord[:-1].lower()] += 1
                        currentWord = ''
                elif(i==' ' or i == '\n' or i == '.' or i == ','or i == ';' or i == '"') and not currentWord[:-1].lower() in dictionaryList:
                        dictionaryList[currentWord[:-1].lower()] = 1
                        currentWord = ''

        cleverName = os.read(currentFile, 100)



del dictionaryList['']
print(dictionaryList)  

currentWriter = os.open("outputKey.txt", os.O_WRONLY | os.O_CREAT |  os.O_TRUNC)


for key in dictionaryList:
        os.write(currentWriter, (str(key)+ ' ').encode())
        os.write(currentWriter, (str(dictionaryList[key])+'\n').encode())


os.close(currentWriter)
