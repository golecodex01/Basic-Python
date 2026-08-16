
num=int(input("enter number "))
sum=0
pro=1
while num>0:
    digit=num%10
    sum=sum+digit
    pro=pro*digit
    num=num//10
print("Difference of Product and Summation is : ",pro-sum)

