num=input("Enter Number : " )

count=0
for i  in range(1,len(num)-1):
   current=int(num[i])
   left=int(num[i-1])
   right=int(num[i+1])
   
   if current==left+right:
       print(current ,end=" ")
       count=count+1
if count==0:
   print("No Matching Digits ")
else:
   print()
   print("Count ",count)
   print("Pattern Found ")