num=input("Enter NUmber ")
i=0
f=0
while i<=len(num):
    if num[i]=='0':
        f=1
        break
    i=i+1
if f==1:
    print("Duck Number ")
else:
    print("Not Duck Number ")