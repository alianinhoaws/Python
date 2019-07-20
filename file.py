
import sys

inputfile = "myfile.txt"
#outputfile = "../"
while True:
    try:
        """start of interception errors"""
        print ("INSIDE TRY")
        myfile = open (inputfile, mode = 'r', encoding = 'Latin_1')
    except Exception:
        """if find errror"""
        print ("Inside EXCEPT")
        print ("find an error")
        print (sys.exc_info() [1])
        """print sys information about error"""
        inputfile = input ("enter correct file name")
        sys.exit
    else:
        """if everithing ok"""
        print (inputfile.read())
        sys.exit