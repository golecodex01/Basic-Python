num1=int(input("Enter 1st Number : "))
num2=int(input("Enter 2nd Number : "))

for i in range(num1,num2+1):
    if i %10==5:
        print(i ,end=" ")
        
