'''8. Count Multiples of 5 Between Two Numbers
A supermarket gives coupons to customers whose token numbers are multiples of 5. The manager enters a token range and wants to know how many eligible token numbers exist.
Write a program to count numbers divisible by 5 between two given numbers using loops.
Input:
1 20
Output:
Count = 4'''

num1=int(input("Enter 1st Number : "))
num2=int(input("Enter 2nd Number : "))
count=0
while num1<=num2:
    if num1%5==0:
        count=count+1
    num1=num1+1
print("Count of Multiples of 5 : ",count)

