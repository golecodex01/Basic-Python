rg=input("Enter Registration Number : ")
count=0
for ch in rg:
   
   if ch>='0' and ch<='9':
      count=count+1
print("Digit Counter is : ",count)