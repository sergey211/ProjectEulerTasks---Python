#task 3 - новое решение
import time
t = time.localtime() 
current_time = time.strftime("%H:%M:%S", t) 
print('time: '+current_time)
#x=13195
x=600851475143 # stalo 53 sec
global found
found = False
global chislo
chislo = 0
for i in range(2,x):
    if found:
        break
    else:
        if x%i == 0:
            y=x/i
            for j in range (2,x+1):
                if found:
                    break
                else:
                    if y%j==0: 
                        for l in range (2,x):
                            if y%l==0:
                                break
                            if l==y-1:
                                chislo=y
                                # print('chislo = '+str(chislo)) 
                                found = True                                
                                break
                        break  
print('iskomoe chislo = '+str(chislo))  
t = time.localtime() 
current_time = time.strftime("%H:%M:%S", t) 
print('time: '+current_time)              