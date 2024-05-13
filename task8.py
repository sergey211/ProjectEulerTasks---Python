str1 = '73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450'
diapazon = 13
list1 = str1.split('0')
print(list1)
print(len(list1))
for i in range(len(list1)):
    if len(list1[i]) < diapazon:
        list1[i] = 0
print('')
print(list1)
while list1.count(0) != 0:
    list1.remove(0)
print('')
print(list1)
print(len(list1))
print('')
count13 = 0
list2 = []
for i in range(len(list1)):
    list2.append(len(list1[i]))
    print(len(list1[i]))
    if len(list1[i]) == 13:
        count13 = count13 + 1
print('count 13=' + str(count13))
print('list2=' + str(list2))
sumj = 0
list3 = []
for i in range(len(list1)):  # ot 0 do 24 (dlina spiska)
    for j in range(len(list1[i])):  # ot 0 do dliny 1-go elementa spiska (13)
        sumj = sumj + int(list1[i][j])
        print('element' + str(i) + ' sum=' + str(sumj))
    print('final element' + str(i) + ' sum=' + str(sumj))
    print('vsego elementov' + str(list2[i]) + ' srednee=' + str(sumj / list2[i]))
    list3.append(sumj / list2[i])
    sumj = 0
print('')
print(list1)
print('')
print(list2)
print('')
print(list3)
print('')
print(max(list3))
posled1 = list1[0]
print('')
print(posled1)
sump1 = 0
proizp1 = 1
for i in range(len(posled1)):
    sump1 = sump1 + int(posled1[i])
    print('sum=' + str(sump1))
    proizp1 = proizp1 * int(posled1[i])
    print('proizv' + str(proizp1))
print('total sum posl 1 = ' + str(sump1))
print('total proizv posl 1 = ' + str(proizp1))
posled1 = list1[2]
sump1 = 0
proizp1 = 1
for i in range(len(posled1)):
    sump1 = sump1 + int(posled1[i])
    print('sum=' + str(sump1))
    proizp1 = proizp1 * int(posled1[i])
    print('proizv' + str(proizp1))
print('total sum posl 1 = ' + str(sump1))
print('total proizv posl 1 = ' + str(proizp1))
maxmaxmax = 0
maxmax = []
index = 0
for w in range(len(list1)):
    posled1 = list1[w]  # 43 digits in string
    print(posled1)
    listelstrns = []
    for i in range(len(posled1) - diapazon + 1):
        print(posled1[i:i + diapazon])
        listelstrns.append(posled1[i:i + diapazon])
    print(listelstrns)
    sump1 = 0
    proizp1 = 1
    sumss = []
    proizvv = []
    for j in range(len(listelstrns)):
        posled1 = listelstrns[j]
        for i in range(len(posled1)):
            sump1 = sump1 + int(posled1[i])
            # print('sum = '+str(sump1))
            proizp1 = proizp1 * int(posled1[i])
            # print('proizv '+str(proizp1))
        print('total sum posled ' + str(j) + ' = ' + str(sump1))
        sumss.append(sump1)
        print('total proizv posled ' + str(j) + ' = ' + str(proizp1))
        proizvv.append(proizp1)
        sump1 = 0
        proizp1 = 1
    print('')
    print(sumss)
    print('')
    print(proizvv)
    print(max(sumss))
    print('max proizved = ' + str(max(proizvv)))
    maxmax.append(max(proizvv))
    if max(proizvv) > maxmaxmax:
        maxmaxmax = max(proizvv)
        index = w
print(list1)
print('')
print(list2)
print('')
print(maxmax)
print('max proizved total = ' + str(maxmaxmax))
print('index=' + str(index))
# 23514624000
