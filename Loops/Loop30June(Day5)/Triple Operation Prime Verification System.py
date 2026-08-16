
import math 
num=int(input("Enter A NUmber" ))
digitsum=0
rev=0
temp=num


while num>0:
    digit=num%10
    rev=rev*10+digit
    digitsum=digitsum+digit
    num=num//10

abdiff=abs(temp-rev)


digitsumandreverse= digitsum+abdiff

print(rev)
print(digitsum)
print(abdiff)
print(digitsumandreverse)



if digitsumandreverse<=1:
    print("Not Prime ",digitsumandreverse)
else:
    i=2
    while i<=temp//2:
        if temp%i==0:
            print("Not Prime ")
            
            break
        temp=temp//2    
    else:
        print("Final Result is Prime Number ")



  