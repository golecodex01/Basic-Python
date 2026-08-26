'''
2.

=========================================
EMPLOYEE DEPARTMENT COUNT
=========================

A company stores employee department names in a list.

employees = ["HR","IT","HR","Sales","IT","IT","Finance"]

Write a program to:

* Count how many employees belong to each department.
* Store the result in a dictionary.

Sample Output:
{'HR': 2, 'IT': 3, 'Sales': 1, 'Finance': 1}

---


'''
#WAY----1
# employees = ["HR","IT","HR","Sales","IT","IT","Finance"]
# freq={}
# for i in employees:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1

# print(freq)

#WAY----2
employees = ["HR","IT","HR","Sales","IT","IT","Finance"]
freq={}
for i in  range(len(employees)):
    ch=employees[i]
    freq[ch]=freq.get(ch,0)+1
print(freq)