# https://leetcode.com/problems/global-and-local-inversions/submissions/
'''
Question 

We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is equal to the number of local inversions.
'''
# gc = 0
# def isIdealPermutation(A):
#     if len(A)==1:
#         return True
#     arr =A
#     def merge(arr, low, mid, high): 
#         global gc
#         i = low
#         j = mid
#         c = []
#         while i < mid and j < high:
#             if arr[i] < arr[j]:
#                 c.append(arr[i])
#                 i += 1
#             else:
#                 gc+=mid-i
#                 c.append(arr[j])
#                 j += 1
#         c.extend(arr[i:mid])
#         c.extend(arr[j:high])
#         return gc


#     def globalCount(arr, low, high):
#         # O(nlogn)
#         if high-low >= 2:
#             mid = (low+high)//2
#             globalCount(arr, low, mid)
#             globalCount(arr, mid, high)
#             return merge(arr, low, mid, high)



#     def localCount(arr,l,h):
#         lc=0
#         for idx in range(h-1):
#             if arr[idx]>arr[idx+1]:
#                 lc+=1
#         return lc
#     globalCount(arr,0,len(arr))
#     ans = gc
#     ans2 = localCount(arr,0,len(arr))
#     print(ans2,ans)
#     return ans==ans2

def isIdealPermutation(A):
    '''Logic 
    To have equal number of local and global
    You should have no global inversion 
    why? gc = lc+ non local inversion
    so you prove non local inversion exists and viola you can make solution O(n)'''
    m = A[0]
    for i, value in enumerate(A[:-2]):
        m = max(m,A[i])
        print(m)
        if m>A[i+2]:
            return False
    return True

if __name__ == "__main__":
    arr = [0,1,2]
    # ans = isIdealPermutation(arr)

    ans = isIdealPermutation(arr)
    # ans2 = localCount(arr,0,len(arr))
    print(ans)
  