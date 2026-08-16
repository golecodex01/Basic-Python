num=int(input("ENter a Number : "))
temp=num 
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
if rev==temp:
    print("Palindrome Number ")
else:
    print("Not Palindrome NUmber ")