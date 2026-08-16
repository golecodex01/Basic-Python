num=int(input("Enter Number : "))
sumeven=0
while num>0:
    digit=num%10
    if digit%2==0:
        sumeven=sumeven+digit
    num=num//10
print("Sum of Even NUmber is : ",sumeven)