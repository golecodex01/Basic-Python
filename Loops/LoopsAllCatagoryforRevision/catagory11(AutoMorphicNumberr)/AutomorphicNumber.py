num=int(input("Enter Number "))
realnum=num
count=0
sqnum=num*num

while num>0:
    if num%10==sqnum%10:
        count=count+1
    num=num//10
    sqnum=sqnum//10

if count==len(str(realnum)):
    print("Automorphic Number ")
else:
    print("Not automorphic Number ")
