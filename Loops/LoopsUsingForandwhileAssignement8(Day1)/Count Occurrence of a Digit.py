'''**11. Count Occurrence of a Digit**
A system logs repeated digits in a number for pattern analysis and reporting.
Write a program to **count how many times a given digit appears in a number using loops**.

Input: Number = 122312, Digit = 2
Output: 3

---'''

num=int(input("Enter A number :"))
digit=int(input("Enter Digit :"))
count=0
while num>0:
    ldigit=num%10
    if ldigit==digit:
        count=count+1
    num=num//10

    
print("Digit ",digit,"is Occurance for ",count,"times ")