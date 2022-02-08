import os,time

load = '█'
count = 0

for t in range(101):
    time.sleep(0.1)
    print(f'\rUnlock File {t}% \033[1;97m[\033[1;92m{load}\033[1;97m]', end='', flush=True)
    count += 1
    if count == 1:
    	count = 0
    	load += '█'
print ("")
print ('Done')
