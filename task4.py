#task4 - palindrom iz 3-zhachnyh mnojitelei
import time
found=False
listi=[]
listj=[]
list1=[]
list2=[]
for i in reversed(range(900,1000)):
    for j in reversed(range(900,1000)):
        proizved=j*i
        print('mnojitel 1 = '+str(i))
        print('mnojitel 2 = '+str(j))
        print('proizved = '+str(proizved))
        revproizv=str(proizved)[::-1]
        print('proizved reversed = '+revproizv)
        if str(proizved) == revproizv:
            print('found palindrom i = '+str(proizved))
            time.sleep(2)
            listi.append(i)
            print('spisok i = '+str(listi))
            listj.append(j)
            print('spisok j = '+str(listj))
            list1.append(proizved)
            print('spisok 1 = '+str(list1))
            time.sleep(2)
#               found = True
#               break
    if str(proizved) == revproizv:
        print('found palindrom j = '+str(proizved))
        time.sleep(2)
        list2.append(proizved)
        print('spisok 1 = '+str(list1))
        print('spisok 2 = '+str(list2))
        time.sleep(2)
        found = True
        break
print('spisok i = '+str(listi))
listj.append(j)
print('spisok j = '+str(listj))
list1.append(proizved)
print('spisok 1 = '+str(list1))
#91 * 99 = 9009     
#995 x 583 = 580085  
#print('max proizved = '+str(max((list1, key=lambda k: int(k))))         
print('iskomoe chislo = '+str(max(list1)))   
# 906609      