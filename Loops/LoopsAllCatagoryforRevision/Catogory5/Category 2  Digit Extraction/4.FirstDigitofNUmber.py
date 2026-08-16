num=int(input("Enter a Number : "))
rev=0
while num>0:
    rev=rev*10+num%10
    num=num//10
    

first=rev%10
print("First Digit is : ",first)