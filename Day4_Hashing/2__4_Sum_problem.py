# https://leetcode.com/problems/4sum/submissions/

# Title : 2__4_Sum_problem
# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note:

# The solution set must not contain duplicate quadruplets.

# Example:

# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]


def fourSum(result, target):
    from itertools import combinations
    result = []
    for i in combinations(nums, 4):
        if sum(i) == target:
            result.append(i)
    return sorted([list(i) for i in result], reverse=1)


def findFourElements(arr, N, target):
    from collections import defaultdict

    # dict can also be used
    hashMap = defaultdict(list)
    result = set()
    for i in range(0, N-1):
        for j in range(i+1, N):
            curPair = (i, j)
            s = arr[i]+arr[j]
            hashMap[s].append(curPair)

            remaining = target-s
            if remaining in hashMap:
                for pair_with_rem in hashMap[remaining]:
                    if len(set(curPair+pair_with_rem)) == 4:
                        result.add(
                            tuple(sorted(map(lambda target: arr[target], curPair+pair_with_rem))))

    return [sorted(i) for i in result]


if __name__ == "__main__":
    target = 0
    nums = [1, 0, -1, 0, -2, 2]
    result = findFourElements(nums, len(nums), target)
    print(
        *result,
        sep='\n'
    )
