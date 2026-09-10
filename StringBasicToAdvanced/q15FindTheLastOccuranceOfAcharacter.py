msg=input("Enter your Message : ")
ch =input("Enter characater to find ")

for i in range(len(msg)):
    if msg[i]==ch:
        continue
print(i)