a=int(input())
def factors(k):
    i=1;sum=0
    while(i<k):
        if k%i==0:
            sum+=i
        i+=1;
    return sum    

p='Perfect Number' if(a==factors(a)) else 'Not a perfect number'
print(p)
flag=0

import math
def isprime(pr):
    for i in range(2,int(math.sqrt(pr))+1):
        if(pr%i==0):
            return False
    return True
    

print("prime") if(isprime(a)==1) else print("not prime")