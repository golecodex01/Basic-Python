num=int(input("Enter a NUmber "))

while num>0:
    digit=num%10
    if digit==0:
        print("Duck NUmber ")
        break
    num=num//10

else:
    print("Not Duck NUmber ")