c=int(input("enter the number:"))
n=0
rev=0
temp=c
if(c>0):
    while(c!=0):
        n=c%10
        rev=rev*10+n
        c//=10

    if(temp==rev ):
          print("its palindrome")
    else:
            print("not a palindrome")
    
else:
    print("not a palindrome")
