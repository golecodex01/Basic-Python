#$5. Palindrome Check
#A number plate is considered special if it reads the same forward and backward. Such numbers are called palindromes.
#Write a program to **check whether a given number is a palindrome using loops**.

#Input: 121
#Output: Palindrome

num=int(input("Enter a Number : "))
rev=0
temp=num
while temp>0:
    rev=rev*10+temp%10
    temp=temp//10

if rev==num:
    print("Polindrome NUmber ")
else:
    print("Not Polindrome ")
