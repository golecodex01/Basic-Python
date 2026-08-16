num=int(input("Enter a Number "))
factcount=0
factsum=0
factPro=1

for i in range(1,num+1):
    if num%i==0:
        print(i)
        factcount=factcount+1
        factsum=factsum+i
        factPro=factPro*i
print("Factors Count : ",factcount)
print("Factors sum : ",factsum)
print("Factors product : ",factPro)
    