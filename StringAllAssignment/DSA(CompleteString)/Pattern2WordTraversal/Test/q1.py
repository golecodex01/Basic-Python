msg=input("ENter your message : ").lower()
word=input("Enter word to find ").lower()
count=0
words=msg.split()

for ch in words:
  if ch==word:
    count=count+1
print("COunt is ",count)