num=int(input("Enter Number : "))
sumodd=0
while num>0:
    digit=num%10
    if digit%2!=0:
        sumodd=sumodd+digit
    num=num//10
print("Sum of Odd Number is : ",sumodd)