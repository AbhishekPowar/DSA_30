# https://leetcode.com/problems/merge-intervals/solution/
# Solution

# Time Complexity O(nlogn)


def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    arr = sorted(intervals)
    if len(arr):
        low = arr[0][0]
        high = arr[0][1]
        ansArray = []
        for nextLow, nextHigh in arr[1:]:
            print(nextLow, nextHigh, high, nextLow > high and nextHigh > high)
            if nextLow <= high:
                if nextHigh > high:
                    high = nextHigh
            elif nextLow > high and nextHigh > high:
                ansArray.append((low, high))
                low = nextLow
                high = nextHigh
        ansArray.append((low, high))
        return ansArray
    else:
        return []
