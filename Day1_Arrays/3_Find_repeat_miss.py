# Repeat and Missing Number
# https://www.hackerrank.com/contests/kcertc/challenges/find-the-repeating-and-the-missing


def findRepeatMissHash(arr):
    """findRepeatMissHash 

    Parameters
    ----------
    arr : int
        Input array

    Returns
    -------
    repeat : int
    miss : int 
        repeat and miss

    TimeComplexity 
    --------------
    O(n)
    """

    repeat = -1
    miss = -1

    d = dict.fromkeys(range(1, len(arr)+1), 0)
    for i in arr:
        d[i] += 1

    for key in d:
        if d[key] == 2:
            repeat = key
        elif d[key] == 0:
            miss = key

    return repeat, miss


def findRepeatMissVisited(arr):
    """findRepeatMissVisited 

    Parameters
    ----------
    arr : int
        input array

    Returns
    -------
    repeat:int
    miss:int
        repeat and miss

    Time Complexity
    ---------------
    O(n)
    """
    repeat = -1
    miss = -1

    arr_len = len(arr)
    visited = [0 for _ in range(arr_len)]

    # Runs 'N' times
    for item in arr:
        if visited[item-1] == 0:
            visited[item-1] = item
        else:
            repeat = item

    # Runs 'N' times
    visited_len = len(visited)
    for idx in range(visited_len):
        if visited[idx] == 0:
            miss = idx+1
    return repeat, miss


def findRepeatMissNoSpace(arr):
    """findRepeatMissNoSpace 

    Parameters
    ----------
    arr : int
        input array

    Returns
    -------
    repeat:int
    miss:int
        repeat and miss

    Time Complexity
    ---------------
    O(n^2)
    """
    arr_len = len(arr)
    for i in range(1, arr_len+1):
        if i not in arr:
            miss = i
            break

    for i in range(arr_len):
        if arr[i] in arr[i+1:]:
            repeat = arr[i]
            break

    return miss, repeat

    # Choose funciton to use here
# findRepeatMiss = findRepeatMissHash
# findRepeatMiss = findRepeatMissVisited
findRepeatMiss = findRepeatMissNoSpace

arr = [3, 1, 3]
miss, repeat = findRepeatMiss(arr)
print(f'Repeat = {repeat}\nMiss = {miss}')


'''
Test case check
'''
# https://www.hackerrank.com/contests/kcertc/challenges/find-the-repeating-and-the-missing
# solution
# N = input()
# arr = list(map(int, input().split(' ')))
# arr_len = len(arr)
# for i in range(1, arr_len+1):
#     if i not in arr:
#         miss = i
#         break

# for i in range(arr_len):
#     if arr[i] in arr[i+1:]:
#         repeat = arr[i]
#         break

# print(miss,repeat,sep=',')
