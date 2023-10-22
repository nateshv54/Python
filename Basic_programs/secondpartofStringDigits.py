import time 
L1=[121,122,123,156,255,111,112,113]
res1=bytes(L1)
print("---Before immutable operations----")
print(*res1)
print()
print("----After immutbale operations----")
res1[0]=101 
print(*res1)
print()
time.sleep(2)
print("End of an application")