

#inputfile = "../"
#outputfile = "../"

frase_toLook = "anything"

myfile1 = open (inputfile, mode = 'r', encoding = 'latin_1')
myfile2 = open (outputfile, mode = 'a', encoding = 'latin_1')

for num,line in enumerate (myfile1,1):
    if frase_toLook in line:
        print ("Line N: "+ str (num) + line.strip())
        myfile2.write ("Found " + line)
    """if find (anything) print it and write to file2 with appending (mode = 'a')"""

myfile1.close()
myfile2.close()
"""close all files"""