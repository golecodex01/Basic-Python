n=int(input("Enter a Number : "))
i=1
while i<=n:
    space=n-i
    while space>0:
        print(" ",end=" ")
        space=space-1
    j=1
    while j<=i:
        if i+j%2==0:
            print("0",end=" ")
            
        else:
            print("1",end=" ")
        j=j+1
    print()
    i=i+1


        
        
        