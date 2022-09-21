st=input().split()
tt=input().split()
l=st+tt
for i in l:
    if((i not in st) or(i not in tt)):
        print(i,end=" ")

