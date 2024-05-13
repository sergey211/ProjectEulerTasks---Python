prv = 1
nxt = 2
chislo = 0
summa = 0
while chislo < 4000000:
    chislo = prv + nxt
    prv = nxt
    nxt = chislo
    if prv % 2 == 0:
        summa = summa + prv
print('summa ' + str(summa))
