
# ====================================================================
# 4. Longest Consecutive Sequence
# ===============================

# Scenario

# Find the longest sequence of consecutive numbers present in the list.

# Requirements

# * Read N and list elements from user
# * Find the length of the longest consecutive sequence
# * Display the sequence length

# Test Case 1

# Input:
# [100, 4, 200, 1, 3, 2]

# Output:
# Longest Consecutive Length = 4

# Explanation:
# Sequence = 1, 2, 3, 4

# Test Case 2

# Input:
# [10, 11, 12, 20]

# Output:
# Longest Consecutive Length = 3

# ---

# ====================================================================
# Q4. Longest Consecutive Sequence
# Scenario:
# Find the longest sequence of consecutive numbers present in the list.
#
# Requirements:
# Read N and list elements from user
# Find the length of the longest consecutive sequence
# Display the sequence length

arr=list(map(int,input("Enter elements: ").split()))
n=len(arr)

high=0

for i in range(n):
    count=1
    current=arr[i]

    while current+1 in arr:
        count=count+1
        current=current+1

    if count>high:
        high=count

print("Longest Consecutive Length =",high)