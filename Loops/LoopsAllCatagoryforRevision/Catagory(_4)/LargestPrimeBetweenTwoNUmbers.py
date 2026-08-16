num1=int(input("Enter 1st Number "))
num2=int(input("Enter second Number "))
largest=-1
while num1<=num2:
    count=0
    for  i in range(1,num1+1):
        if num1%i==0:
            count=count+1
    if count==2:
        if num1>largest:
            largest=num1
    num1=num1+1

if largest==-1:
    print("No Prime Numbers Lies Between Two Numbers")
else:
    print("Largest Prime ",largest)
