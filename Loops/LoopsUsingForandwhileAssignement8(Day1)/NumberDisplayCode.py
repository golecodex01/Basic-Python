
'''**13. Number Range Display System (if-elif with loops)**
A number analysis tool processes two input values and displays numbers between them based on their relationship.

* If the first number is less than the second, display numbers in ascending order
* If the first number is greater than the second, display numbers in descending order
* If both numbers are equal, display "Both numbers are same"

Write a program using **if-elif-else and loops** to implement this logic.

Input: 5, 10
Output: 5 6 7 8 9 10

Input: 10, 5
Output: 10 9 8 7 6 5

Input: 7, 7
Output: Both numbers are same


14.Floor Movement System (Elevator)
An elevator system takes the current floor and destination floor as input.

If current floor < destination → move upward and display floors
If current floor > destination → move downward and display floors
If both are same → display "Already on the same floor"

Write a program using if-elif-else and loops to simulate elevator movement.

Input: 1, 5
Output: 1 → 2 → 3 → 4 → 5

Input: 7, 3
Output: 7 → 6 → 5 → 4 → 3

Input: 4, 4
Output: Already on the same floor
'''

num1=int(input("ENter 1st Number :"))
num2=int(input("ENter 2nd Number :"))
if num1<num2:
    print("Num2 is greater than num2 ")
    while num1<=num2 :
        print(num1 , end=" ")
        num1=num1+1


elif num1>num2:
    print("Num1 is greater than num2")
     while num1>=num2 :
        print(num1 , end=" ")
        num1=num1-1
    
else:
    print("Both Numbers are Same ")
    print(num1,num2)