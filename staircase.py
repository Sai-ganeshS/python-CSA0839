n=int(input())
one=1
two=1

for i in range(1,n):
    t=one
    one=one+two
    two=t

print(one)
    
