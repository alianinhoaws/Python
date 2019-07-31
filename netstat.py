#netstat proc
import os
lst = os.popen('sudo netstat -tulpn').read()
lst = lst.split('\n')
for i in range(2,len(lst)):
    print(lst[i])
