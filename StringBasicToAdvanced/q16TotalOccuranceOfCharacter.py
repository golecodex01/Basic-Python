msg=input("Enter your Message : ")
ch=input("Enter your cahracter to find : ")
count=0
for i in msg:
    if i==ch:
        count+=1

print("Total Occurance of Character is : ",count)