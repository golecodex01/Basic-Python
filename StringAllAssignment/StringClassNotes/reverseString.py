num=input("Enter String : ")
start=0
rev=""
end=len(num)-1
while end>=start:
    rev=rev+num[end]
    end=end-1
if rev==num:
    print("Yes ")
print(rev)