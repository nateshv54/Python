import pickle
import  train1
import train2
f1=open("train_info.txt","rb")
while(True):
    try:
        
        obj1=pickle.load(f1)
        obj1.m1()

    except EOFError as e:
        print("Exception name: ",e)
        break

f1.close()
