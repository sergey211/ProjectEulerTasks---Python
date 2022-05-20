import time
a=331
b=332
c=337
print('sum='+str(a+b+c))
print('a^2+b^2='+str(a*a+b*b))
print('c^2='+str(c*c))
'''
vozmem a = 1
togda b = ot 1 do 500
i c = 1000-a-b
'''
global x
found=False
for a in range (1,1000):
    if not found:
        for b in range (a+1,1000):
            if not found:
                c=1000-a-b
                print('a='+str(a))
                print('b='+str(b))
                print('c='+str(c))
                abSquare=a*a+b*b
                cSquare=c*c
                print('sum='+str(a+b+c))
                print('a^2+b^2='+str(abSquare))
                print('c^2='+str(cSquare))
                if abSquare==cSquare and b<c:
                    time.sleep(2)
                    found=True
                    x=a #pri vyhode iz cykla a = 999 ????
                    break
a=x
print('a='+str(a))
print('b='+str(b))
print('c='+str(c))
print('a*b*c='+str(a*b*c))
#31875000