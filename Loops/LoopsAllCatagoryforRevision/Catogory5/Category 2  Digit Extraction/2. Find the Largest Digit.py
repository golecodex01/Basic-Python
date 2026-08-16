num=int(input("ENter a Number : "))
lar=num%10
while num>0:
    digit=num%10
    if digit>lar:
        lar=digit
    num=num//10
print("Largest Number is : ",lar)