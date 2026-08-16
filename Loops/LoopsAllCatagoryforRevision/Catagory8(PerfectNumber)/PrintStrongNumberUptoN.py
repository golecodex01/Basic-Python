num=int(input("Enter N : "))
i=1
while i<=num:
    temp=i
    sum=0
    while temp>0:
        digit=temp%10
        fact=1
        temp=temp//10
        for j in range(1,digit+1):
            fact=fact*j
        sum=sum+fact
    if sum==i:
        print(i ,end=" ")
    i=i+1
