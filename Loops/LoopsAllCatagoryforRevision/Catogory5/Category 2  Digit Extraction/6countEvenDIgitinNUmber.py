n=int(input("ENter a Number : "))
c=0
while n>0:
    digit=n%10
    if digit%2==0:
        c=c+1
    n=n//10
print("Even Digit Count is : ",c )
