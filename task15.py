# https://euler.jakumo.org/problems/view/15.html
import random

star = [0, 0]
finished = False
counter = 0
predel = 7
popytki = 10000
interv = 200


def find_way(start):
    way = []
    while start != [predel, predel]:
        if (start[0] < predel) and (start[1] < predel):
            numb = random.randint(0, 1)
            start[numb] += 1
        elif start[0] == predel:
            start[1] += 1
        elif start[1] == predel:
            start[0] += 1
        my_mas = [start[0], start[1]]
        way.append(my_mas)
    return way


ways = []
mas1 = find_way([0, 0])
ways.append(mas1)
counter = 0
while counter < popytki:
    counter += 1
    if counter % interv == 0:
        print('tries = ', counter)
        print('ways = ', len(ways))
    mas = find_way([0, 0])
    for i in range(0, len(ways)):
        way = ways[i]
        if mas == way:
            break
        else:
            if i == len(ways)-1:
                ways.append(mas)

print()
for way in sorted(ways):
    print(way)
print('predel = ', predel)
print('popytki = ', popytki)
print('kol-vo marshrutov = ', len(ways))

# map (find_way(), 3)

# predel =  10
# popytki =  30000
# kol-vo marshrutov =  23189



# 3 = 20
# 4 = 70
# 5 = 252
# 6 = 924
# 7 = 3250
# 8 = 9516 (30 000 popytok)
# 9 = 30000
# 10 = 90000
# 11 = 270000
# 12 = 810000

# 20 =

# array[a, b]
# array[a, b+1]
# array[a+1, b_finished]
# array[a_finished, b_finished]

# array[a, b]
# array[a, b+1]
# array[a+1, b_finished-1]
# array[a+1, b_finished]
# array[a_finished, b_finished]

# array[a, b]
# array[a, b+1]
# array[a+1, b_finished-2]
# array[a+1, b_finished-1]
# array[a+1, b_finished]
# array[a_finished, b_finished]



