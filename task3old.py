# task 3 - он рабочий но понадобится около 50 часов на моем буке для его выполнения
list1 = []
# x=13195
# x=12312312
x = 600851475143
for i in range(2, x):
    if x % i == 0:
        list1.append(i)
        print(i)
print('spisok delitelei: ' + str(list1))
print('dlina spiska: ' + str(len(list1)))
print('end')
for j in range(0, len(list1)):
    for k in range(2, list1[j]):  # ot 2 (chtob ne del na 1) do znachenia prostogo chisla
        # (5, 7, 13, 29, 35)
        if list1[j] % k == 0:  # берем элемент списка и делим его на все
            # значения от 2 до этого числа
            print('element ' + str(list1[j]))
            print('delitel ' + str(k))
            list1[j] = 0
            print('spisok new: ' + str(list1))
            break
while list1.count(0) != 0:
    list1.remove(0)
    print('spisok new: ' + str(list1))
print('poslednii element = ' + str(list1[-1]))
