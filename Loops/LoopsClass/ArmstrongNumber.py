num=int(input("Enter a Number :"))
temp=num
power=len(str(num))
digitSum=0
while num>0:
    lastdigit=num%10
    powerDigit=lastdigit**power
    digitSum=digitSum+powerDigit
    num=num//10
if temp==digitSum:
    print("It is Armstrong NUmber because NUmber is ",temp,"and DigitSum is ",digitSum)
else:
    print("It is NOT Armstrong NUmber because NUmber is ",temp,"and DigitSum is ",digitSum )