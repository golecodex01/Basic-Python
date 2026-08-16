num1=int(input("Enter 1st NUmber "))
num2=int(input("Enter 2nd Number "))

if num1>num2:
    small=num2
else:
    small=num1
for i in range(1,small+1):
    if num1%i==0 and num2%i==0:
        print(i ,end=" ")
