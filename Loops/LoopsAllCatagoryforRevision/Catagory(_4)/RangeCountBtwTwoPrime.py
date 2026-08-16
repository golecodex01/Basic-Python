num1=int(input("Enter 1st Number "))
num2=int(input("Enter 2nd Number "))

primecount=0

while num1<=num2:
    count=0
    for i in range(1,num1+1):
        if num1%i==0:
            count=count+1
    if count==2:
        primecount=primecount+1
        
    num1=num1+1

print("Prime Count ",primecount)


