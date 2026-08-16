

name=input("Enter name of the Student : ").lower()

count=0
vocount=0
for i in name :
    if i in "aeiou":
        vocount=vocount+1
    else:
        count=count+1

print("Total Consonant Count : ",count)
print("Total Vovel Count : ",vocount)
