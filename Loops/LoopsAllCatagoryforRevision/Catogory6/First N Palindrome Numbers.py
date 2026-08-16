n=int(input("Enter N : "))

for i in range(0,n+1):
    temp=i
    rev=0
    while temp>0:
       
        rev=rev*10+i%10
        temp=temp//10
    if i==rev:
        print(i , end=" ")


