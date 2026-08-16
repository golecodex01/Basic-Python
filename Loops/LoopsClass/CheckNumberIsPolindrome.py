num=int(input("Enter A NUmber :"))
rev=0
temp=num
while num>0:
    rev=rev*10+num%10
    num=num//10
if rev==temp:
    print("It is Polindrome ")
else:
    print("Not Polindrome ")