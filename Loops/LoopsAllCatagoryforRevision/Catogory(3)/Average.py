num=int(input("ENter a Number : "))
sum=0
t=len(str(num))
while num>0:
    digit=num%10
    sum=sum+digit
    num=num//10
av=sum/t
print("Average is : ",av)
