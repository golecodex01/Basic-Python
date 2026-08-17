# 4.
# Palindrome Number List Checker
# Scenario

# A system checks lucky numbers which are palindromes.

# Requirements
# Check palindrome numbers
# Store palindrome numbers in list
# Count palindrome numbers
# Find largest palindrome
# Sort palindrome list
# Test Cases

# Input:
# [121, 131, 20, 44, 55, 100]

# Output:

# Palindromes: [121, 131, 44, 55]
# Count: 4
# Largest: 131
# Sorted: [44, 55, 121, 131]

l=list(map(int,input("enter a list").split()))
large=0
pal=[]
count=0
for i in l:
    rev=0
    num=i
    temp=i
    while num>0:
        r=num%10
        rev=rev*10+r
        num=num//10
    if temp==rev:
        pal.append(i)
        count=count+1
        if i>large:
            large=i
print("Palindromes ",pal)
print("Count ",count)
print("Largest ",large)
pal.sort()
print("Sorted ",pal)