'''2. Smallest Digit in Number
A manufacturing company prints serial numbers on products. During quality testing, the scanner needs to detect the smallest digit in the serial number to verify coding standards.
Write a program to find the smallest digit in a number using loops.

Input:




Output:
Smallest Digit = 2
'''


num=int(input("Enter a Number  : "))
small=9
while num>0:
    digit=num%10
    if small>digit:
        small=digit
    num=num//10
print("Smallest Digit is : ",small)