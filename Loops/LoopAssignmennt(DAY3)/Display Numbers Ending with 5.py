'''3. Display Numbers Ending with 5

A supermarket tracks token numbers ending in 5.
Write a program using loops to display numbers ending with 5 between two numbers.

Input:
10 40

Output:
15 25 35


'''
num1=int(input("Enter 1st Nunmber :" ))
num2=int(input("Enter 2nd Number : "))

while num1<=num2:
    if num1%10==5:
        print(num1 ,end=" ")
    num1=num1+1
