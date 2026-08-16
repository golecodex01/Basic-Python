'''
3. First Digit of Number
A university receives thousands of application IDs. The first digit of each ID represents the department code, so the admission software must read the first digit quickly.
Write a program to find the first digit of a number using loops.

Input:
53892

Output:
First Digit = 5'''



num=int(input("Enter Number : "))
rev=0
while num>0:
    rev=rev*10+num%10
    num=num//10

fdigit=rev%10
print("First Digit is : ",fdigit)