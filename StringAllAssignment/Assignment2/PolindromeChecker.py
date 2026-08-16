'''5.
Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.

Input:
Enter product code: MADAM

Output:
Palindrome Code

Input:
Enter product code: PRODUCT

Output:
Not a Palindrome Code
'''
code=input("Enter Product code ").lower()


rev=""
start=0
end=len(code)-1
while end>=start:
    rev=rev+code[end]
    end=end-1

    

if  rev.lower()==code:
    print("Polindrome ")
else:
    print("Not Polindrome ")