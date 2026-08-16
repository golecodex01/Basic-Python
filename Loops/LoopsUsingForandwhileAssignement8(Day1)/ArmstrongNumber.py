
#6. Armstrong Number (3-digit)
#In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
#EWrite a program to **check whether a number is an Armstrong number using loops**.

#Input: 153
#Output: Armstrong

num=int(input("Enter a number :"))
sum=0
temp=num
power=len(str(num))
while num>0:
    digit=num%10
    sum=sum+digit**power
    num=num//10
if temp==sum:
    print("Armstrong Number ")
else:
    print("Not a ArmStrong NUmber ")