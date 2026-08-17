# 5.

# Rearrange the array in alternating positive and negative items
# Given an unsorted array Arr of N positive and negative numbers.
# Your task is to create an array of alternate positive and negative numbers
# without changing the relative order of positive and negative numbers.
# Note: Array should start with positive number.

# Example 1:
# Input:
# N = 9
# Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}
# Output:
# 9 -2 4 -1 5 -5 0 -3 2
# Example 2:
# Input:
# N = 10
# Arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
# Output:
# 5 -5 2 -2 4 -8 7 1 8 0
# Rearrange array in alternating positive and negative items

n=int(input("Enter N: "))
arr=list(map(int,input("Enter elements: ").split()))

positive=[]
negative=[]

for i in range(n):
    if arr[i]>=0:
        positive.append(arr[i])
    else:
        negative.append(arr[i])

i=0
j=0

while i<len(positive) and j<len(negative):
    print(positive[i],end=" ")
    print(negative[j],end=" ")
    i=i+1
    j=j+1

while i<len(positive):
    print(positive[i],end=" ")
    i=i+1

while j<len(negative):
    print(negative[j],end=" ")
    j=j+1