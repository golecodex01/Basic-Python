text=input("Enter message ")
current=""
longest=""

for ch in text:
    count=0
    for i in current:
        if ch==i:
            COunt=count+1
        if count==0:
            current=current+ch
        else:
            current=ch
        
        if len(current)>len(longest):
            longest=current

print("Longest Substring",longest)
print("Length",len(longest))