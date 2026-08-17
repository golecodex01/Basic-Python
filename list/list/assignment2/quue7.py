
# 7.
# Factory Production – Factorial Expansion List

# Problem Statement

# A factory produces items where production capacity is defined using factorial growth.

# Given a list of numbers, replace each number with its factorial value.

# Then perform analysis on the resulting list.

# Tasks:

# Convert each element to factorial
# Find sum of all factorial values
# Find maximum factorial value
# Count how many factorial values are even

# Input:
# A list of integers

# Example 1

# Input:
# [3, 4, 5]

# Processing:
# 3! = 6
# 4! = 24
# 5! = 120

# Output:
# [6, 24, 120]
# Sum = 150
# Max = 120
# Even Count = 3
l=list(map(int,input("enter a list: ").split()))
new=[]
sum=0
maxi=0
count=0

for i in l:
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    new.append(fact)
    sum=sum+fact
    if fact>maxi:
        maxi=fact
    if fact%2==0:
        count=count+1

print(new)
print("Sum =",sum)
print("Max =",maxi)
print("Even Count =",count)