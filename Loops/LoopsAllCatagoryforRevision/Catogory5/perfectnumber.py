num=int(input("Enter number "))
factsum=0
for i in range(1,num):
    if num%i==0:
        factsum=factsum+i
if factsum==num:
    print("Perfect Number ")
else:
    print("Not Perfect NUmber ")

if factsum>num:
    print("Abundand Number ")
else:
    print("Not Abundance ")