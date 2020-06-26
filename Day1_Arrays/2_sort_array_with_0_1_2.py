# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0
# Given an array A of size N containing 0s, 1s, and 2s; you need to sort the array in ascending order.

# Input:
# The first line contains an integer 'T' denoting the total number of test cases. Then T testcases follow. Each testcases contains two lines of input. The first line denotes the size of the array N. The second lines contains the elements of the array A separated by spaces.

# Output:
# For each testcase, print the sorted array.

# Input :
# 2
# 5
# 0 2 1 2 0
# 3
# 0 1 0

# Output:
# 0 0 1 2 2
# 0 0 1

# Explanation:
# Testcase 1: After segragating the 0s, 1s and 2s, we have 0 0 1 2 2 which shown in the output.
# TimeComplexity
# O(n)
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

l = 0
m = 0
h = len(arr)-1
while m <= h:
    item = arr[m]
    if item == 0:
        print(f'\t\titem arr[{m}] = {arr[m]} swapped with arr[{l}] = {arr[l]}')
        arr[l], arr[m] = arr[m], arr[l]
        l += 1
        m += 1
    elif item == 1:
        m += 1
    else:
        arr[h], arr[m] = arr[m], arr[h]
        h -= 1
    print(f'Array')
    print(f'\t\t', *arr)
