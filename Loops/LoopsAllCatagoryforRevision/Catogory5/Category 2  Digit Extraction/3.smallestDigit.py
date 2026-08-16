num=int(input("Enter a NUmber : "))
small=num%10
while num>0:
    digit=num%10
    if digit<small:
        small=digit
    num=num//10
print("Smallest Number is : ",small)