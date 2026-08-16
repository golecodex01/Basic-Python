n=int(input("Enter a Number :"))
i=1
while i<=n:
     j=1
     while j<=i:
           print(j ,end=" ")
           j=j+1
     star=1
     while star<=2*(n-i):
           print("*" , end=" ") 
           star=star+1

     k=i
     while k>=1:
           print(k , end=" ")
           k=k-1
     i=i+1
     print()
      
   
