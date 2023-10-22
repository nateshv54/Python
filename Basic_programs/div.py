c=input()
b=int(input())
d=int(input())

print((c*b)[::-1])

def fact(a):
    if(a<=0):
        return 1;
    return a*fact(a-1)

def div(b,d):
    if(d==0):
        return "Zero by division error"
    return "Floor division is",format(b//d) ,"Division is",format(b/d)

print(div(b,d))