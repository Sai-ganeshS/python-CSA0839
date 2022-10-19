s=input().split()
s1=input().split()
s2=s+s1
for i in s2:
    if((i not in s) or (i not in s1)):
        print(i,end=' ')
