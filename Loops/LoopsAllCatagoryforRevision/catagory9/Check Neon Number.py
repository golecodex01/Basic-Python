num=int(input("Enter Number : "))

sq=num*num
temp=sq
sum=0
while temp>0:
    digit=temp%10
    
    sum=sum+digit
    temp=temp//10
if sum==num:
    print("Neon Number ")
else:
    print("Not Neon Number ")