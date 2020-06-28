# https://leetcode.com/problems/excel-sheet-column-number/
#1_Excel_Column_Number
# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 

# O(m)
# My solution
def titleToNumber(s: str) -> int:
    letter_map = {chr(asc):asc-ord('A')+1 for asc in range(ord('A'),ord('Z')+1)}
    numeric = 0
    s_len = s.__len__()
    for idx,val in enumerate(s):
        numeric+= letter_map[val]*(26**(s_len-1-idx))
    return numeric

# Time = O(n) 
# Inspired
def better(s):
    ans = 0
    for i in s:
        ans = ans*26 + (ord(i)-64)
    return ans
ans = better('AAA')  