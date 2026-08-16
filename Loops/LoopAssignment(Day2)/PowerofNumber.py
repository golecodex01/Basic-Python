'''7. Power of a Number
A scientific calculator app is used by engineering students for repeated multiplication operations. It should calculate the value of a number raised to a given power.
Write a program to calculate n raised to power p using loops.

Input:
2 5

Output:
32
'''

num=int(input("Enter a Number : "))
power=int(input("Enter power : "))
p=1
i=1
while i<=power:
    p=p*num
    i=i+1
print("number is : ",p)
