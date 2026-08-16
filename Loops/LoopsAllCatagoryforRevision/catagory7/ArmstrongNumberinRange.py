num1=int(input("Enter 1st NUmber "))
num2=int(input("Enter 2nd Number "))

count=0

while num1<=num2:
    temp=num1
    sum=0
    
    while temp>0:
        
        cube=0
        d=temp%10
        cube=d*d*d
        sum=sum+cube
        temp=temp//10
    if num1==sum:
        print(num1 ,end=" ")
        count=count+1
       
    num1=num1+1
print("Count ",count)