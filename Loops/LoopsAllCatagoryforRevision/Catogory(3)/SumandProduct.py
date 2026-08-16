num=int(input("enter number "))
sum=0
pro=1
while num>0:
    digit=num%10
    sum=sum+digit
    pro=pro*digit
    num=num//10
print("Summation is : ",sum)
print("Product is : ",pro)