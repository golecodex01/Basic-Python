num=int(input("Enter Number "))
temp=num
sum=0
while num>0:
    digit=num%10
    cube=digit**3
    sum=cube+sum
    num=num//10
if sum==temp:
    print("YEs Armstrong ")
else:
    print("Not Armstrong ")
