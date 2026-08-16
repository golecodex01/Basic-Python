'''
3.
Word Counter in Complaint Message

A customer care system wants to count how many words are present in a complaint message.

Input:
Enter complaint: Delivery was delayed again today

Output:
Total words: 5
'''
'''
com=input("Enter complaint : ")

com=com.strip()
countspace=0
for ch in com:
    if ch==" ":
        countspace=countspace+1

print("Total words: ",countspace+1)

'''

msg=input("Enter Message : ")
count=0
previous=" "
for ch in msg:
    if ch!=" " and previous==" ":
        count=count+1
    previous=ch
print("Word Count in MESSAGE : ",count)

