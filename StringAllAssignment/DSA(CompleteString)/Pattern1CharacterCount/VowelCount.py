rg=input("Vowel Counter : ")
count=0
for ch in rg:
   
   if ch.lower() in "aioue":
      count=count+1
print("Wovel Counter is : ",count)