'''A science lab studies whether digits are in increasing order.
Write a program using for-else loop:
- If every next digit is greater than previous print Stable Number
- Else Unstable Number
Input:
12359
Output:
Stable Number
'''




num=int(input("Enter a Number :"))
x=0
rev=0

while num<0:
    lastdigit=num%10
    rev=rev*10+ lastdigit
    num=num//10

temp=rev 
while rev>0:
    lastDigit=rev%10
    rev=rev//10
    previousDigit=rev%10

    if lastDigit< previousDigit :
        x=x+1

m=len(str(temp))+1  
if x==m :
    print("Stable Number ")
else:
    print("Unstable Number ")


