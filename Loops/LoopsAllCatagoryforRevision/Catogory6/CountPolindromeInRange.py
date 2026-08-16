num1=int(input("Enter 1st Number :"))
num2=int(input("ENter 2nd Number : "))
sum=0
for i in range(num1,num2+1):
    temp=i
    rev=0
    while temp>0:
        rev=rev*10+temp%10
        temp=temp//10
    if rev==i:
        sum=sum+i
    
print("Sum  is ",sum)

