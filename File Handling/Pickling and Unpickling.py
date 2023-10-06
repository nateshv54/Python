import time,pickle
 #input data
my_data={'Bmw',1001,'Toyoto','Benz'}

#pickle the input
with open("file2.pickle","wb") as f1:
    pickle.dump(my_data,f1)
    
#unpickling
with open("file2.pickle","rb") as f2:
    res=pickle.load(f2)
    print(res)
