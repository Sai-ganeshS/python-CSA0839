t=int(input())
if(t<=0):
    print("invalid")
    
else:
    e=[int(i) for i in input().split()]
    l=[int(i) for i in input().split()]
    if(len(e)==t and len(l)==t):
         k=0
         ll=[]
         for i in range(len(e)):
    
             if(i==0):
                ll.append(e[i]-l[i])
                k=e[i]-l[i]
             else:
        
                ll.append(abs(k+e[i]-l[i]))
                k=k+e[i]-l[i]
        
    else:
        print("invalid")
   
print(max(ll))     


