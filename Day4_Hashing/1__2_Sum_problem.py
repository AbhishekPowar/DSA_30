# https://leetcode.com/problems/two-sum/submissions/
# 1__2_Sum_problem

# TimeComplexity
# O(n)


def twoSum(nums, target):
    arr = nums
    arr_inv_map = {}
    for i in range(len(arr)):
        if arr_inv_map.get(arr[i], 'X') == 'X':
            arr_inv_map[target-arr[i]] = i
        else:
            return arr_inv_map[arr[i]], i


if __name__ == "__main__":
    arr = [2, 7, 3, 9, 1]
    target = 10
    m, n = twoSum(arr, target)
