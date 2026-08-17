# 8. Majority Element Detector
# ============================

# Scenario

# Find an element occurring more than N/2 times.

# Requirements

# * Read N and list elements from user
# * Find majority element
# * If not present, display appropriate message

# Test Case 1

# Input:
# [2, 2, 1, 2, 3, 2, 2]

# Output:
# Majority Element = 2

# Test Case 2

# Input:
# [1, 2, 3, 4]

# Output:
# No Majority Element Found

# ---
# Q8. Majority Element Detector

arr=list(map(int,input("Enter elements: ").split()))
n=len(arr)

found=False

for i in range(n):
    count=0

    for j in range(n):
        if arr[i]==arr[j]:
            count=count+1

    if count>n/2:
        print("Majority Element =",arr[i])
        found=True
        break

if found==False:
    print("No Majority Element Found")

