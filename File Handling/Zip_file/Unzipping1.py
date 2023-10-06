from zipfile import *
f1=ZipFile("zip1.zip",'r',ZIP_STORED)
s1=f1.namelist()
'''for x1 in s1:
    print("Filename is",x1)
    f2=open(x1,'r')
    obj=f2.read()
    print(obj)'''
print(s1)