'''
6.

Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

Conditions:
- Ignore spaces
- Ignore case sensitivity

Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room

Output:
Both Product Codes are Matching

'''
p1=input("Enter First product code : ").lower()
p2=input("Enter second product code : ").lower()

p1=p1.replace(" ","").lower()
p2=p2.replace(" ","").lower()

if sorted(p1)==sorted(p2):
    print("Both Product Codes are Macthing ")
else:
    print("Not Matched ")

