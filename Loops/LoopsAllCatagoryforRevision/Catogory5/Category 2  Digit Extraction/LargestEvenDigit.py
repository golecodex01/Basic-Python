num=int(input("ENter a NUmber : "))
largest=-1
while num>0:
    digit=num%10
    if digit%2==0:
        if digit>largest:
            largest=digit
    num=num//10
if largest==-1:
    print("No Even Digiit found ")
else:
    print("Largest even digit is : ",largest)