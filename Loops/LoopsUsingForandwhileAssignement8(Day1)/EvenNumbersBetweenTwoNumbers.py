'''**10. Even Numbers Between Two Numbers**
A teacher wants to assign only even roll numbers for a special activity. The system should display all even numbers between two given numbers.
Write a program to **display all even numbers between two numbers using loops**.

Input: 10, 20
Output: 10 12 14 16 18 20'''

num1=int(input("Enter 1st number "))
num2=int(input("Enter 2nd number "))

while num1<=num2:
    if num1%2==0:
        print(num1 ,end=" ")
    num1=num1+1
