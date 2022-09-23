nums=[int(i) for i in input().split()]
m=[]
for i in nums:
    count=0
    for j in nums:
        if(j<i):
            count+=1

    m.append(count)
    

    

print(m)
        
