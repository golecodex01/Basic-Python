'''4. Strong Number Checker
A digital lock opens only for strong numbers.
A strong number is a number whose sum of factorial of digits equals the number.
Example:
145 = 1! + 4! + 5!
Write a program using loops to check strong number.
Input:
145
Output:
Strong Number
'''
num=int(input("Enter a NUmber : "))
temp=num
sum=0
while num>0:
    digit=num%10
    fact=1
    while digit>0:
        fact=fact*digit
        digit=digit-1
    sum=sum+fact
    num=num//10
if sum==temp:
    print("Strong Number ")
else:
    print("Not Strong Numberr ")
    