import time
class A:pass 
class B(A):pass 
class C(A):pass 
class D(B,C):pass 
print()
print("====MRO OF A CLASS ====")
print(A.mro())
print()
print("====MRO OF B CLASS=====")
print(B.mro())
print()
print("====MRO OF C CLASS====")
print(C.mro())
print()
print("====MRO OF D CLASS====")
print(D.mro())
print()
time.sleep(2)
print("End of an application")

'''
====MRO OF A CLASS ====
[<class '__main__.A'>, <class 'object'>]

====MRO OF B CLASS=====
[<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

====MRO OF C CLASS====
[<class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

====MRO OF D CLASS====
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

End of an application

'''