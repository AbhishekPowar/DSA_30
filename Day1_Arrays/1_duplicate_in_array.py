# Find the duplicate in an array of N integers.
# https://leetcode.com/problems/find-the-duplicate-number/


def FindDuplicateHash(arr):
    """removeDuplicateHash 

    Parameters
    ----------
    arr : int 
        input array

    Returns
    -------
    newArr
        Array with unique elements

    Time Complexity
    --------------
    O(n)
    """
    arrMap = {}
    for i in arr:
        arrMap[i] = arrMap.get(i, 0)+1

    return list(filter(lambda item: arrMap[item] > 1, arrMap))


def FindDuplicateNoSpace(arr):
    """FindDuplicateNoSpace 

    Parameters
    ----------
    arr : any
        Input array

    Returns
    -------
    newArr
        Array with unique elements

    Time Complexity
    ---------------
    O(n^2)
    """
    arr_len = arr.__len__()
    newArr = []
    for idx in range(arr_len):
        if arr[idx] not in arr[idx]:
            newArr.append(arr[idx])

    return newArr


if __name__ == "__main__":
    FindDuplicate = FindDuplicateHash
    FindDuplicate = FindDuplicateNoSpace

    arr = [1, 2, 7, 6, 3, 2, 7, 8]
    uniqueArr = FindDuplicateHash(arr)

# https://leetcode.com/problems/find-the-duplicate-number/
# Leetcode ans:
# nums_map = dict()
#         for i in nums:
#             nums_map[i] = nums_map.get(i,0)+1

#         for i in nums_map:
#             if nums_map[i] > 1:
#                 return i
#         return -1
