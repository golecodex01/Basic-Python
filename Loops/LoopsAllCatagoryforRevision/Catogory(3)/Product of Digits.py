num=int(input("Enter Number "))
pro=1
while num>0:
    digit=num%10
    pro=pro*digit
    num=num//10
print("Product is ",pro)
