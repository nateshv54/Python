from zipfile import *
f1=ZipFile("zip1.zip","w",ZIP_DEFLATED)
f2=open('otp.txt','w')
f1.write("otp.txt")
f3=open('number.txt','w')
f1.write("number.txt")
f4=open('email.txt','w')
f1.write("email.txt")
print("Zip folder created successfully")