# https://leetcode.com/problems/next-permutation/submissions/
# Input → Output
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    arr = nums
    N = len(arr)
    start = -1
    for i in range(N-1, 0, -1):
        if arr[i] > arr[i-1]:
            start = i-1
            break
    if start >= 0:
        mini = arr[start+1]
        idx = start+1
        for i in range(start+1, N):
            if arr[i] > arr[start] and mini >= arr[i]:
                mini = arr[i]
                idx = i
                # break
        arr[start], arr[idx] = arr[idx], arr[start]
        arr[start+1:] = arr[N-1:start:-1]
    else:
        arr[:] = arr[::-1]


if __name__ == "__main__":
    arr = [8, 9, 7]
    nextPermutation(arr)
    print(arr)
