import json
d1={}
d1['pid']=1001
d1['pname']="Mobile1"
d1['price']=24000
d1['company']='Samsung'
d1['Product_status']=True
d1['Product_is_there']=None
with open('file1.txt','w') as f:
    json.dump(d1,f)
    print("\n Object Serialization Done successfully ")