'''A smart locker accepts only numbers whose all digits are unique.
Write a program using for-else loop to:
- Check every digit
- If any repeated digit found reject

- Else accept
Input:
57294
Output:

Valid Unique Code'''

num=int(input("Enter A number "))
temp=num

while temp>0:
    digit=temp%10
    temp=temp//10
    m=str(digit)
    n=str(temp) 
    if m in n :
        print("Not Valid ")
        break
else:
    print("Valid............")





print("Using For Loop...................")
num2=int(input("Enter A number :"))
temp2=num2
for i in range (len(str(num2))):
    m=str(temp2%10)
    n=str(temp2//10)

    if m in n :
        print("Not Valid........")
        break
else:
    print("Valid ..........")