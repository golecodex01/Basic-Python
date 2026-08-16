num=input("Enter NUmber ")
res=0
sum=0
lar=0
for i in range(1,len(num)):
    res=(int(num[i])-int(num[i-1]))
    res=abs(res)
    if res>lar:
        lar=res
    sum+=res
    print(res,end=" ")
    
print(sum)
print(lar)