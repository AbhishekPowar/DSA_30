# 3__Longest_Consecutive_Sequence


def longestConsecutive(nums):
    arr = nums
    hashMap = set(arr)
    maxi = 0
    for i in hashMap:
        if i-1 not in hashMap:
            k = i
            c = 0
            while k in hashMap:
                k += 1
                c += 1
            maxi = max(c, maxi)
    return maxi


if __name__ == "__main__":
    # Input: [100, 4, 200, 1, 3, 2]
    # Output: 4
    # Explanation:
    # The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
    arr = [100, 4, 200, 1, 3, 2]
    ans = longestConsecutive(arr)

    # If sorted
    # arr = [1, 2, 3,  8, 9, 11, 12,13,14]
    # maxi = 1
    # c = 1
    # for i in range(1, len(arr)):
    #     if arr[i]-arr[i-1] == 1:
    #         c += 1
    #     else:
    #         maxi = max(maxi, c)
    #         c = 1
    # maxi = max(maxi, c)
    # print(maxi)
