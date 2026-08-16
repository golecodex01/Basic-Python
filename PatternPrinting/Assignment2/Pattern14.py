n=int(input("Enter a NUmber :"))
i=1

while i<=n:
    space=n-i
    while space>0:
        print(" ",end="")
        space=space-1
    
    j=1
    while j<=i:
         print("*", end="" )
         j=j+1
  
    i=i+1
    print()
