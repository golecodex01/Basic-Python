
n=int(input("Enter a NUmber "))

s=0

while n>0:
    s=s+n%10
    n=n//100

print("Alternate Sum =",s)

c=0
for i in range(1,s+1):
    if s%i==0:
        c=c+1

if c==2:
    print("Prime")
else:
    print("Not Prime")