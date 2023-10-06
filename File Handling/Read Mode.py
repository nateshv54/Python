import os
if os.path.isfile('file1.txt'):
    print('File Exists')
    f1=open('file1.txt')
    print("File mode is :",f1.mode)
