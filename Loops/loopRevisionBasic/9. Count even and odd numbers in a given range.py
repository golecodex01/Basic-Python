num=int(input("Enter a NUmber : "))
i=1
evencounter=0
oddcounter=0
while i<=num:
    if i%2==0:
        evencounter=evencounter+1
    else:
        oddcounter=oddcounter+1
    i=i+1
print("Even Count is : ",evencounter)
print("Odd Count is : ",oddcounter) 