import time
counter=1
found = False
print(time.strftime("%H:%M:%S", time.localtime()))
for i in range (2,100000000):
    if not found:
        for x in range(2,i):
            if i%x==0:
                break
            else:
                if x==i-1:
                    counter=counter+1
                    if counter%1000==0:
                        print(time.strftime("%H:%M:%S", time.localtime()))
                        print(str(counter)+'='+str(i))
                        time.sleep(1)
                    if counter==10001:
                        print('iskomoe chislo='+str(i))
                        found=True
                        break