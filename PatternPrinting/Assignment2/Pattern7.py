n=int(input("Enter a Number :"))
i=1
while i<=n:
     j=1
     while j<=i:
           if i%2==0:
              print("*" , end=" ")
           else:
              print(j , end=" ")
           j=j+1
     i=i+1
     print()

              
