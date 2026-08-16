num=int(input("Enter Number "))
nextArm=num+1

while True:
    sum=0
    c=0
    temp=nextArm
    while temp>0:
        digit=temp%10
        c=digit**3
        sum=sum+c
        temp=temp//10
    if sum==nextArm:
        print("NExt Arm : ",nextArm)
        break
    nextArm=nextArm+1


