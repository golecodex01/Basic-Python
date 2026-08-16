


import math 
num=int(input("Enterr a Number "))
digitsum=0
pro=1



while num>0:
    digit=num%10
  
    digitsum=digitsum+digit
    pro=pro*digit
    num=num//10

diproandsum= pro-digitsum
count=len(str(diproandsum))

print("Sum ",digitsum)
print("Product ",pro)
print("Difference",diproandsum)
print("Digits ",count)



fnumber=diproandsum+int(count)
temp=fnumber
print("Final Result",fnumber)

if fnumber<=1:
    print("Not Prime Number ")
else:
    i=2
    while i>=fnumber//2:
        if temp%i==0:
            print("Not Prime ")
            break
        i=i+1
    else:
        print("Prime Number ")









'''
Input:

234


Output:

Sum = 9

Product = 24

Difference = 15

Digits = 2

Final Result = 17

Prime
'''