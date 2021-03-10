'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

def addTwoNums(List1,List2):
    process = ''
    output = 0
    for n in List1[-1:-1:-1]:
        process += str(n) 
    process += ' '
    for n in List2[-1:-1:-1]:
        process += str(n)    
    for n in process.split(' '):
        output += int(n)
    return [d for d in output[-1:-1:-1]]

print(addTwoNums([2,4,3],[5,6,4]))