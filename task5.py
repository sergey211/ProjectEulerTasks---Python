#2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
#Какое самое маленькое число делится нацело на все числа от 1 до 20?
import time
t = time.localtime() 
t1 = time.time() 
current_time = time.strftime("%H:%M:%S", t) 
print('time: '+current_time)
diapazon = 18
print('diapazon = '+str(diapazon))
global found 
found = False
for i in range(1,300000000):
    if found:
        break
    else:
        for j in reversed(range(2,diapazon+1)):
            if i%j!=0:
                break
            else:
                if j==2:
                    chislo=i
                    print(chislo)
                    found = True
                    break
print('iskomoe chislo = '+str(chislo))  
t = time.localtime() 
current_time = time.strftime("%H:%M:%S", t) 
t2 = time.time()
t3=t2-t1
work_time = time.gmtime(t3) 
print('time: '+current_time)   
print('время работы скрипта: '+str(work_time.tm_min)+' min '+str(work_time.tm_sec)+' sec')  
#232792560
