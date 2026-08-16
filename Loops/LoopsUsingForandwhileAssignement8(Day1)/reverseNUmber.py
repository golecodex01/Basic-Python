#4. Reverse a Number

#A security system stores OTP codes in reverse format for encryption to increase data safety. Reversing a number means extracting digits and rebuilding it in reverse order.
#Write a program to **reverse a given integer using loops**.

#Input: 1234
#output: 4321

num=int(input("Enter A number : "))
rev=0
while num>0:
    lastdigit=num%10
    rev=rev*10+lastdigit
    num=num//10
print("Reversed NUmber is : ",rev)