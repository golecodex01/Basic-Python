num=int(input("Enter a Number :"))
digitSum=0
while num>0:
    lastdigit=num%10
    digitSquare=lastdigit*lastdigit
    digitSum=digitSum+digitSquare
    num=num//10
if digitSum%2==0:
    print("Sum of squares of digit is Even that is ",digitSum)
else:
    print("Sum of squares of digit is Odd that is ",digitSum)
