import sys
import os

x = len(sys.argv)

if x > 1:
    if sys.argv[1] == "/?":
        print ("Enter an argument to desolve")
    print ("Arguments added: " + str(sys.argv[1:]))
else:
    print ("write arg")

os.system ("ls -la")
os.mkdir ("list")
sys.exit(2)