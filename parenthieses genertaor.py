import itertools
n=int(input())
l=[]
for i in range(n*2):
    if(i<n):
        l.append("(")
    else:
        l.append(")")
L=list(itertools.permutations(l,n*2))
x=[]
m=set(L)

for i in list(m):
    s=[]
    for j in list(i):
        if(j=="("):
            s.append(1)
        else:
            if(len(s)==0):
                s.append(1)
                break
            else:
                s.pop()
    if(len(s)==0):
        x.append(i)
for i in x:
    print(list(i)," ",end=' ')
        
