num=int(input("Enter A Number :"))

factSum=0
i=1
while i<num:
    if num%i==0:
        factSum=factSum+i 
    i=i+1
if num==factSum:
    print("It is Perfect Number ")

else:
    print("Not a Perfect Number ")