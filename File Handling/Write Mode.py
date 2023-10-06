#Write Mode
f1=open("file1.txt","w")
print("File Information")
print("FileName is :",f1.name)
print("File Mode is: ",f1.mode)
print("File Closed: ",f1.closed)
print("File Readable :",f1.readable())
print("File writable : ",f1.writable())

print("Writing into the file")
f1.write("Python is most demanding Language")