# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# 5__Remove_Duplicate_from_Sorted_array


def removeDuplicates(self, nums: List[int]) -> int:
    if not nums:
        return 0
    l = 0
    one = nums[l]
    for h in range(len(nums)):
        if nums[h] > nums[h-1]:
            nums[l] = nums[h]
            l += 1
    nums.insert(0, one)
    return l+1

# def removeDuplicates(arr, n):
#     if n == 0 or n == 1:
#         return n

#     for i in range(0, n-1):
#         if arr[i] != arr[i+1]:
#             arr[j] = arr[i]
#             j += 1

#     arr[j] = arr[n-1]
#     j += 1
#     return j
