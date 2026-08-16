num=int(input("Enter Number : "))
temp=num
digitsum=0
while temp>0:
    digit=temp%10
    digitsum=digitsum+digit
    temp=temp//10
if num%digitsum==0:
    print("Harshad NUmber ")
else:
    print("Not Harshad NUmber ")