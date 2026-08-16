num=input("Enter Number : ")
evencount=0
lar=0
firstdif=-1
same=True
for i in range(0,len(num)-1):
    current=int(num[i])
    next=int(num[i+1])
    dif=abs(next-current)
    print(dif ,end=" ")
    
    if dif%2==0:
       evencount=evencount+1
    if dif>lar:
       lar=dif
    if i==0:
       firstdif=dif
    elif dif!=firstdif:
       same=False
print()
print("Max Difference : ",lar)
if same:
     print("uniform ")
else :
     print("Not Uniform ")
       
    
