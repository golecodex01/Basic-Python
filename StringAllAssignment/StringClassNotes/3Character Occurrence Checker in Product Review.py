review=input("Enter CUstomner Review : ")
count=0
ch=input("Enter character to Check Occurance : ").lower()

for i in review.lower():
    if i==ch:
        count=count+1
print("Total Occurance : ",count)