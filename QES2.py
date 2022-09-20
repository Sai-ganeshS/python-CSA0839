def sumsq(l,n):
    even=0
    odd=0
    while(n>0):
        i=int(input("enter the program"))
        if(i%2==0):
            even=even+i**2
        else:
            odd=odd+i**2
        n=n-1

        
    l=[odd,even]
    return(l)
    




n=int(input("enter the no element:"))
l=[]
print(sumsq(l,n))
