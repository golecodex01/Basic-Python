num=int(input("Enter Number : "))
proeven=1
while num>0:
    digit=num%10
    if digit%2==0:
        proeven=proeven*digit
    num=num//10
print("Product of Even NUmber is : ",proeven)