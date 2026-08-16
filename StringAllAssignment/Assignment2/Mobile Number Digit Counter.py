'''
2.
Mobile Number Digit Counter

A telecom company wants to count how many digits are present in a customer contact number entered with spaces or symbols.

Input:
Enter contact number: +91 98765-43210

Output:
Total digits: 12

'''
number=input("Enter Mobile NUmber ")
count=0
for ch in number:
    if ch.isdigit():
       count=count+1

print("Digits count is : ",count)