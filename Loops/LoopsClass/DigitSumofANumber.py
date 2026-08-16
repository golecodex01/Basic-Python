num=int(input("Enter a Number :"))
digitSum=0
count=0
while num>0:
    digit=num%10
    count=count+1
    digitSum=digitSum+digit
    num=num//10

print("Digit Sum OF Number Is :", digitSum)
print("Digit Count is :", count)


