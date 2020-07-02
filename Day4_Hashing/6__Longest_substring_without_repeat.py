# https://www.interviewbit.com/problems/longest-substring-without-repeat/
# 6__Longest_substring_without_repeat


# The longest substring without repeating letters
# for "abcabcbb" is "abc", which the length is 3.

# For "bbbbb" the longest substring is "b",
#  with the length of 1.
from collections import defaultdict

# O(n^2)


def solve(string):
    hashset = len(set(string))
    ans = 1
    for curLen in range(hashset, 1, -1):
        f = 0
        for idx in range(len(string)-curLen):
            sub = string[idx:idx+curLen]
            if len(set(sub)) == curLen:
                return curLen

# O(n)


def maxNonRepeat(string):
    hashMap = defaultdict(int)
    low = 0
    high = 0
    maxDistinct = 0
    for letter in string:
        while hashMap[letter] == 1:
            hashMap[string[low]] -= 1
            low += 1
        hashMap[letter] += 1
        high += 1
        maxDistinct = max(maxDistinct, high-low)
    return maxDistinct


if __name__ == "__main__":

    s = 'abbbbbbbb'
    ans = maxNonRepeat(s)
    print(ans)

    # O(n)
    ans2 = solve(s)
    print(ans2)
