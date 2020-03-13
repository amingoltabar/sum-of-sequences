#cos(x)= 1 - (x**2)/2! + (x**4)/4! - (x**6)/6! + ...
n=int(input('enter the number of sequences '))
x=float(input('enter the amount of x '))
s=0
k=1
for i in range(0,2*n-1,2):
    f=1
    for j in range(1,i+1):
        f*=j
    s+=k*(x**i)/f
    k*=-1
print('summation = ',s)
                                                    
