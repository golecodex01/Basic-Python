num1=int(input("enter any number"))
num2=int(input("enter any number"))

sumprime=0
while num1<=num2:
    count=0
    for i in range(1,num1+1):
        if num1%i==0:
            count=count+1
    if count==2:
        sumprime=sumprime+num1
    num1=num1+1
print(sumprime)