num1=int(input("Enter Number 1 : "))
num2=int(input("Enter Number 2 : "))

count=0
while num1<=num2:
    temp=num1
    factsum=0
    
    while temp>0:
        digit=temp%10
        fact=1
        for i in range(1,digit+1):
            fact=fact*i
        factsum=factsum+fact
        temp=temp//10
    if factsum==num1:
        count=count+1
    num1=num1+1
print("Count of Strong Number is  : ",count)

