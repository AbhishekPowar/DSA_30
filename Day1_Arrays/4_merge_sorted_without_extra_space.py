# Question
# Merge two sorted Arrays without extra space
# https://leetcode.com/problems/merge-sorted-array


# Working
# a = [1,3,5]
# b= [2,4,6]
# After Merge
#  a =  [1,2,3]
#  b =  [4,5,6]
#
# O(m*n)
# def mergeArray(arr1,arr2):
#     index1 = 0
#     index2 = 0
#     arr1_len = len(arr1) 
#     arr2_len = len(arr2)
#     count = 0
#     while index1 < arr1_len and index2 < arr2_len:
#         if arr1[index1] > arr2[index2]:
#             arr1[index1], arr2[index2] = arr2[index2], arr1[index1]
#             insert_index = index2
#             while insert_index+1 < arr2_len and arr2[insert_index] > arr2[insert_index+1]:
#                 count += 1
#                 arr2[insert_index], arr2[insert_index +
#                                         1] = arr2[insert_index+1], arr2[insert_index]
#                 insert_index += 1
#         index1 += 1

#         print(f'''
#         arr1 = {arr1}
#         arr2 = {arr2}
#         index1 = {index1}
#         index2 = {index2}
#         ''')


# arr1 = [8, 9, 11]
# arr2 = [1, 3, 4, 6]
# mergeArray(arr1,arr2)


# Leetcode way
# Working
# a = [1,3,5,0,0,0]
# b= [2,4,6]
# After Merge
#  a =  [1,2,3,4,5,6]
#  b =  [4,5,6]
#
# https://leetcode.com/problems/merge-sorted-array solution
# O(m*n)
def merge(arr1, m, arr2, n) -> None:
    actual_arr1_len = m
    arr1_len = len(arr1)
    arr2_len = n

    insert_index = 0
    for item2 in arr2:
        for index1 in range(insert_index, actual_arr1_len):
            if item2 < arr1[index1]:
                arr1[index1], item2 = item2, arr1[index1]
        arr1[actual_arr1_len] = item2
        actual_arr1_len += 1


arr1 = [1, 2, 3]
arr2 = [2, 5, 6]
len1 = arr1.__len__()
len2 = arr2.__len__()
arr1.extend([0 for _ in arr2])
merge(arr1, len1, arr2, len2)
print(arr1)
