'''1.  Bank Customer Account Privacy System

A national bank is developing a secure customer portal where account
numbers should not be displayed completely on the screen. For security
reasons, the system should hide all digits except the last four digits
before showing them to users.

Conditions: - Display only the last 4 digits - Replace all previous
characters with *

Input: Enter account number: 123456789012

Output: Masked Account: ********9012
'''

'''This is my code 
account=input("Enter account number: ")
ans=""
r=len(account)-4
for i in range(0,r):
    ans=ans+"*"

for j in range(r,len(account)):
    ans=ans+account[j]

print(ans)

'''
account=input("Enter account number: ")
ans=""
for i in range(len(account)):
    if i<=len(account)-4:
        ans=ans+"*"
    else:
        ans=ans+account[i]
print(ans)