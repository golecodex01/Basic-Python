msg=input("Enter feedback Message ")
count=0

for ch in msg.lower():
  
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' :
        count=count+1

print("Vowel count in Feedback : ",count)
