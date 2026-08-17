
# 5.
#  Student Grade Classification System (Python List Assignment)


# A school stores student marks in a list. The system must analyze the marks and generate a **clear performance report**
# by grouping students into grade categories.



# Write a Python program to:

# * Iterate through the list of marks
# * Assign grades based on marks:

#   * **>= 90 → A**
#   * **>= 75 and < 90 → B**
#   * **>= 50 and < 75 → C**
#   * **< 50 → Fail**
# * Store each category in separate lists
# * Count students in each category
# * Display a **final structured report (important)**

# ---

# ## 📌 Output Format (Mandatory)

# Your output must be displayed exactly in this format:

# ```
# ===== STUDENT GRADE REPORT =====

# A Grade Students   : [list]
# B Grade Students   : [list]
# C Grade Students   : [list]
# Fail Students      : [list]

# --------------------------------
# A Count   : X
# B Count   : X
# C Count   : X
# Fail Count: X
# --------------------------------

# Total Students: X
# ```

# ---

#  Input

# [95, 82, 67, 45, 30]

# Output

# ```
# ===== STUDENT GRADE REPORT =====

# A Grade Students   : [95]
# B Grade Students   : [82]
# C Grade Students   : [67]
# Fail Students      : [45, 30]

# --------------------------------
# A Count   : 1
# B Count   : 1
# C Count   : 1
# Fail Count: 2
# --------------------------------

# Total Students: 5



# l=list(map(int,input("Enter marks: ").split()))
# a=[]
# b=[]
# c=[]
# fail=[]
# acount=0
# bcount=0
# ccount=0
# failcount=0

# for i in l:
#     if i>=90:
#         a.append(i)
#         acount=acount+1
#     elif i>=75:
#         b.append(i)
#         bcount=bcount+1
#     elif i>=50:
#         c.append(i)
#         ccount=ccount+1
#     else:
#         fail.append(i)
#         failcount=failcount+1

# print("===== STUDENT GRADE REPORT =====")
# print()
# print("A Grade Students   :",a)
# print("B Grade Students   :",b)
# print("C Grade Students   :",c)
# print("Fail Students      :",fail)
# print("--------------------------------")
# print("A Count   :",acount)
# print("B Count   :",bcount)
# print("C Count   :",ccount)
# print("Fail Count:",failcount)
# print("--------------------------------")
# print("Total Students:",len(l))





l=list(map(int,input("enter a list of marks").split()))
A=[]
B=[]
C=[]
fail=[]
counta=0
countb=0
countc=0
countf=0
for i in l:
    if i>=90:
        A.append(i)
        counta=counta+1
    elif i>=75 and i<90:
        B.append(i)
        countb=countb+1
    elif i>=50 and i<75:
        C.append(i)
        countc=countc+1
    else:
        fail.append(i)
        countf=countf+1
print("A Grade Students   :",A)
print("B Grade Students   :",B)
print("c Grade Students   :",C)
print("fail students   :",fail)

print("A Count   : ",counta)
print("B Count   :",countb)
print("C Count   :",countc)
print("Fail Count:",countf)