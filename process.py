import os
pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]

for pid in pids:
    try:
        print open(os.path.join('/proc', pid, 'cmdline'), 'rb').read().split('\0')
    except IOError: # proc has already terminated
        continue
