
m=int(input())

if m==1:
    a=int(input())
    b=int(input())
    for i in range(a,b+1):
        print(i,end=" ")

elif m==2:
    a=int(input())
    b=int(input())
    for i in range(a,b-1,-1):
        print(i,end=" ")

elif m==3:
    a=int(input())
    for i in range(0,a+1,2):
        print(i,end=" ")

else:
    for i in range(4):
        print("Emergency Alarm")