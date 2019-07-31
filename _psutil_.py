import psutil


while True:
    process_count = psutil.pids()
    print (len(process_count))

#+add result to resi api http 