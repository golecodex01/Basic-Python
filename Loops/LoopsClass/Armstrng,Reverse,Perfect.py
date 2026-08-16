num=int(input("Enter a Number :"))
temp=num
power=len(str(num))
digitSum=0
rev=0
sum=0
while num>0:
    lastdigit=num%10
    rev=rev*10+ lastdigit
    powerDigit=lastdigit**power
    digitSum=digitSum+powerDigit
    num=num//10
if temp==digitSum:
    print("It is Armstrong NUmber ")
else:
    print("It is NOT Armstrong NUmber" )
i=1
temp1=rev
while i<rev//2:
    if rev%i==2:
        sum=sum+i
    i=i+1

print("Reverse Number of Actual NUmber is ",temp1)
if temp1==sum:
    print("reverse of Actual Number  is Perfect Number ")
else:
    print("reverse of Actual Number  is Not Perfect NUmber ")
