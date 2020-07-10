# https://leetcode.com/problems/max-consecutive-ones/submissions/
# 6__Max_continuous_number_of_1’s


def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    maxx = 0
    c = 0
    for i in nums:
        if i == 1:
            c += 1
        else:
            maxx = max(maxx, c)
            c = 0
    maxx = max(maxx, c)
    return maxx
