num=int(input("Enter Number "))
nextStrong=num+1
while True:
    temp=nextStrong
    sum=0
    while temp>0:
        digit=temp%10
        fact=1
        temp=temp//10
        for i  in range(1,digit+1):
            fact=fact*i 
        sum=sum+fact
    if sum==nextStrong:
        print("Next Strong ",nextStrong)
        break
    nextStrong=nextStrong+1

