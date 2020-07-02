# https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1
# 4__Longest_Subarray_with_0_sum
# Input
# 15 -2 2 -8 1 7 10 23

# Output
# 5


def maxLen(n, arr):
    # Code here
    hash_map = {}
    curSum = 0
    maxx = 0
    hash_map[0] = -1

    for idx in range(len(arr)):
        curSum += arr[idx]

        if curSum in hash_map:
            maxx = max(maxx, idx-hash_map[curSum])
        else:
            hash_map[curSum] = idx

    # print(maxx)
    return maxx


if __name__ == "__main__":
    arr = [15, -2, 2, -8, 1, 7, 10, 23]
    ans = maxLen(len(arr), arr)
    print(ans)

    # O(n^2) to understand how it works
    # arr2 = arr[:]
    # key = 9
    # for idx in range(1, len(arr)):
    #     arr[idx] += arr[idx-1]
    # maxx = -sys.maxsize
    # for s in range(0, len(arr)):
    #     for e in range(0, len(arr)):
    #         if s-1 == -1:
    #             summ = arr[e]
    #         else:
    #             summ = arr[e]-arr[s-1]
    #         if summ == key:
    #             print(arr2[s:e+1], summ)
    #             maxx = max(maxx, e-s)

    # print(maxx)
