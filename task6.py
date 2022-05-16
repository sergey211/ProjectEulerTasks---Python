sumofsq = 0
sqofsum = 0
diapazon=101
for i in range (diapazon):
    sumofsq = sumofsq+i*i
print('sum of squares='+str(sumofsq))
for j in range (diapazon):
    sqofsum = sqofsum+j
sqofsum=sqofsum*sqofsum
print('square of sums='+str(sqofsum))
raznica=sqofsum-sumofsq
print('raznica='+str(raznica))