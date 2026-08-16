num=int(input("ENter Number : "))
factsum=0
temp=num
while temp>0:
    digit=temp%10
    fact=1
    for i in range(1,digit+1):
        fact=fact*i 
    factsum=factsum+fact
    temp=temp//10

if factsum==num:
    print("Strong Number ")
else:
    print("Not Strong Number ")