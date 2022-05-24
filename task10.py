import time
#sum=2 #norm gran i/5
sum=-4 #gran = i/7
counter=1
#diapazon=100000 #1 min 16 sec = 454396537
diapazon=200000 #
#diapazon=100000 # gran = i/4 - 0 min 55 sec = 454396537
#diapazon=100000 # gran = i/5 - 0 min 41 sec = 454396537
#diapazon=100000 # gran = i/7 - 0 min 27 sec = 454396543 - на 6 больше
#diapazon=100000 # gran = i/9 - 0 min 21 sec = 454396617 - на 80 больше
#diapazon=500000 #
t = time.localtime() 
t1 = time.time() 
current_time = time.strftime("%H:%M:%S", t) 
print(time.strftime("%H:%M:%S", time.localtime()))
for i in range (2,diapazon): # берем цифру из нашего диапазона
   # gran=round(i/3)+1
    gran=round(i/7)+1
    for j in range (2,gran+1): # и делим ее на все числа от 2 до нее самой
        if i%j!=0: # если это число не делится без остатка
            if j==gran: # и дошло до грани, то ок, иначе .. 
                # print('prostoe:'+str(i))
                sum=sum+i
                # print('summa = '+str(sum))
                counter=counter+1
                if counter%100==0:
                    print('i = '+str(i))
                    print('summa = '+str(sum))
                # time.sleep(1)
                break # .. иначе выходим из цикла
        else:
            break
print('task 101, okonchatelnaya summa = '+str(sum))
t = time.localtime() 
current_time = time.strftime("%H:%M:%S", t) 
t2 = time.time()
t3=t2-t1
work_time = time.gmtime(t3) 
print('time: '+current_time)   
print('время работы скрипта: '+str(work_time.tm_hour)+' hours '+str(work_time.tm_min)+' min '+str(work_time.tm_sec)+' sec')     
#13-38 - 16-08 - 2h 30 min
#142913828922