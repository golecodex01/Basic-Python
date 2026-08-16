num=int(input("ENter "))

primecount=0
prime=1
sum=0
while True:
    
    count=0
    for i in range(1,prime+1):
        if prime%i==0:
            count=count+1
            
    if count==2:
        sum=sum+prime
        primecount=primecount+1
    if primecount==num:
        break
    prime=prime+1 
print("Summation Is : ",sum)