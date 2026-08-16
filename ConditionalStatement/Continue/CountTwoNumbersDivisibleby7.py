num1=int(input("Enter 1st Number : "))
num2=int(input("Enter 2nd Number : "))
count=0
for i in range(num1,num2+1):
    if i%7==0:
        count=count+1
print("COunt Of Number Divisible by 7 ",count)        
