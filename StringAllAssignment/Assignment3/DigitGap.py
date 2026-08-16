num=input("Enter YOur Number ")
count=0
maxdif=0
for i in range(len(num)-1):
    current=int(num[i])
    next=int(num[i+1])
    dif=abs(current-next)
    print(dif ,end=" ")
    
    if dif>2:
       count=count+1
    if dif>maxdif:
       maxdif=dif
print()
print("COunt(>2)=",count)
print("MaxDiifff",maxdif)
if count>2:
    print()
    print("Irrregular ")
else:
    print("Smooth Number ")