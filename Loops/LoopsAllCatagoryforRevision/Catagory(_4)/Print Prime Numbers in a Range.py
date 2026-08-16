num1=int(input("Enter 1st NUmber :"))
num2=int(input("Enter 2nd Number : "))


if num1<num2:
     while num1<=num2:
           count=0
           for i in range(1,num2+1):
                if num1%i==0:
                   count=count+1
           if count==2:
                print(num1 ,end =" ")
           num1=num1+1
elif num2<num1:
    while num2<=num1:
           count=0
           for i in range(1,num1+1):
                if num2%i==0:
                   count=count+1
           if count==2:
                print(num2 ,end =" ")
           num2=num2+1
else:
    print("Both NUmbers are Eq.........")
