'''1. Product of Odd Numbers up to N

A puzzle game rewards players by multiplying odd numbers up to n.
Write a program using loops to find product of odd numbers.

Input:
5

Output:
15'''

num=int(input("Enter a NUmber : "))
pro=1
i=1
while i<=num:
    if i%2!=0:
        pro=pro*i
    i=i+1
print("Product of Numbers Upto N : ",pro) 