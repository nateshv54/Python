m=int(input())
n=int(input())
hcf=1
def factors(m,n):
    for i in range(1,min(m,n)):
        if m%i==0 and n%i==0:
            hcf=i
    return hcf        
        
print("HCF of",m,"and",n,"is ",factors(m,n))

#Recursive Function

def rhcf(m,n):
    if(m==0 or n==0):
        return m+n
    if(m>n):
        return rhcf(m-n,n)
    else:
        return rhcf(m,n-m)

#print(rhcf(m,n))


#lcm function 
lcm=(m*n)//rhcf(m,n)
print("Lcm is ",lcm)
