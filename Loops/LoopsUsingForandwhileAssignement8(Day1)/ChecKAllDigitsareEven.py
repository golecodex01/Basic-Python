'''**9. Check All Digits Are Even**
A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
Write a program to **check whether all digits of a number are even using loops**.

Input: 2468
Output: All Even

Input: 2456
Output: Not All Even
'''
num=int(input("Enter a Number :"))
x=0
while num>0:
    digit=num%10
    if digit%2!=0:
        x=1
    num=num//10
if x==1:
    print("Not all DIgits In Number Is Even ")
else:
     print("All DIgits In Number Is Even ")
    
