# https://www.interviewbit.com/problems/subarray-with-given-xor/

# 5__Count_number_of_subarrays_with_given_XOR(this_clears_a_lot_of_problems)

from collections import defaultdict
from functools import reduce


def visualize(arr, m):
    print(f'Valid subarray with xor = {m}')
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            val = arr[i:j+1]
            ans = reduce(lambda x, y: x ^ y, val)
            if ans == m:
                print(val)


def solve(arr, m):
    from collections import defaultdict
    hashMap = defaultdict(int)
    hashMap[0] += 1
    cur = 0
    x = 0
    for i in arr:
        cur ^= i
        hashMap[cur] += 1
        # print(f'hashmap = {dict(hashMap)}  \nm^cur = {m^cur} \ncur = {cur}\n\n')
        x += hashMap.get(m ^ cur, 0)
    return x


if __name__ == "__main__":
    arr = [5, 2, 1, 4, 6, 3]
    m = 5
    visualize(arr, m)
    print(f'Number of subarray with xor = {m} is {solve(arr,m)}')
