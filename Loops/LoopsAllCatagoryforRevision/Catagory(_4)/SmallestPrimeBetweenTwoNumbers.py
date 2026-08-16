num1=int(input("Enter 1st Number "))
num2=int(input("Enter second Number "))
Smallest=num2
while num1<=num2:
    count=0
    for  i in range(1,num1+1):
        if num1%i==0:
            count=count+1
    if count==2:
        if Smallest>num1:
            Smallest=num1
    num1=num1+1

if Smallest==-1:
    print("No Prime Numbers Lies Between Two Numbers")
else:
    print("Smallest Prime ",Smallest)
