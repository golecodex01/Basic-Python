num=int(input("ENter a Number : "))
n=int(input("ENter number to count Occurance : "))
count=0
while num>0:
    if n==num%10:
        count=count+1
    num=num//10
print("Occurance of ",n,"in ",num,"is ",count)