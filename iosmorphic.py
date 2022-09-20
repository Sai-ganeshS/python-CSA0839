st=input("enter the first string:")
tt=input("enter the second string:")

if(len(st)!=len(tt)):
    print("false")
else:
    d={}
    for i in range(len(st)):
        if(st[i] not in d):
            d[st[i]]=tt[i]
            
    em=""
    for i in range(len(st)):
         em=em+d[st[i]]
    if(em==tt):
        print("true")
         

    
            
    
    
