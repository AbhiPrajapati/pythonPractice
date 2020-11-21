myfile = open("/home/abhishek/Desktop/pythonPractice/fileInPython/newfile.txt","r")
# array of lines
#print(myfile.readlines())
#array of words
for lines in myfile:
    words = lines.split("e")
    print(str(words[0]))
myfile.close()