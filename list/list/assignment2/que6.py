
# 6.

# A security system logs employee entry IDs during a day.

# Only prime-numbered IDs are considered valid VIP entries.

# Tasks:

# Extract all prime IDs from the list
# Find the sum of prime IDs
# Find the maximum prime ID
# Count how many prime entries exist

# Input:
# A list of integers (may contain duplicates and non-prime numbers)

# Example 1

# Input:
# [12, 5, 7, 9, 11, 14, 17]

# Output:
# Prime IDs = [5, 7, 11, 17]
# Sum = 40
# Max = 17
# Count = 4

# Example 2

# Input:
# [4, 6, 8, 10]

# Output:
# Prime IDs = []
# Sum = 0
# Max = -1
# Count = 0

l=list(map(int,input().split()))
prime=[]
sum=0
maxi=-1
count=0

for i in l:
    if i>1:
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c=c+1
        if c==2:
            prime.append(i)
            sum=sum+i
            count=count+1
            if i>maxi:
                maxi=i

print("Prime IDs =",prime)
print("Sum =",sum)
print("Max =",maxi)
print("Count =",count)