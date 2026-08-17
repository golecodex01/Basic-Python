# 10. Find Duplicate Numbers
# ==========================

# Scenario

# A company stores employee IDs in a list. Some IDs may appear more than once due to data entry errors.

# Requirements

# * Read N and list elements from user
# * Find all duplicate numbers
# * Store duplicates in another list
# * Count total duplicate numbers
# * Display duplicates in sorted order

# Test Case 1

# Input:
# [1, 2, 3, 2, 4, 5, 1]

# Output:
# Duplicate Numbers = [1, 2]
# Count = 2

# Test Case 2

# Input:
# [10, 20, 30]

# Output:
# No Duplicate Numbers Found

# ---
# Q10. Find Duplicate Numbers
# Scenario:
# Find all duplicate numbers in the list.
# Store duplicates in another list.
# Count total duplicate numbers.
# Display duplicates in sorted order.

arr=list(map(int,input("Enter elements: ").split()))
n=len(arr)

duplicate=[]

for i in range(n):
    count=0

    for j in range(n):
        if arr[i]==arr[j]:
            count=count+1

    if count>1 and arr[i] not in duplicate:
        duplicate.append(arr[i])

if len(duplicate)==0:
    print("No Duplicate Numbers Found")
else:
    duplicate.sort()
    print("Duplicate Numbers =",duplicate)
    print("Count =",len(duplicate))