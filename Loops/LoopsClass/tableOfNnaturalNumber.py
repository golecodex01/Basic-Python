num=int(input("Enter A Number :"))
temp=num
count=1
for i in range(temp,(num*10+1),num):
    print(num,"*",count,"=",i)
    count=count+1