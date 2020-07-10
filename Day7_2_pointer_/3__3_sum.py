# https://leetcode.com/problems/3sum/submissions/
# 3__3_sum


def threeSum(self, nums: List[int]) -> List[List[int]]:
    arr = sorted(nums)
    n = len(arr)
    res = []
    for i in range(n-2):
        if i == 0 or arr[i] != arr[i-1]:
            print(arr[i])
            target = -arr[i]
            low = i+1
            high = n-1
            while low < high:
                summ = arr[low]+arr[high]
                if summ == target:
                    val = (-target, arr[low], arr[high])
                    res.append(val)
                    low += 1
                    high -= 1
                elif summ < target:
                    low += 1
                else:
                    high -= 1

    return set(res)
