i=int(input("enter the year:"))
if(i%4==0 and i%100!=0):
    print("leap")
else:
    print("its not a leap year")
    for n in range (i,i-4,-1):
        if(n%4==0 and n%100!=0):
            print("the previous year",n)
       
      
