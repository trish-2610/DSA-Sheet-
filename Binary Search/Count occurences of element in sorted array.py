# def first_last_occurrences(arr,target):

#     def find(arr,target,is_first):
#         left = 0
#         right = len(arr) - 1 
#         ans_find = -1
#         while left <= right:
#             mid = left + (right - left) // 2
#             if arr[mid] == target:
#                 ans_find = mid 
#                 if is_first:
#                     right = mid - 1 ## search on left
#                 else:
#                     left = mid + 1 ## search on right 
#             elif arr[mid] < target:
#                 left = mid + 1 
#             else:
#                 right = mid - 1 
#         return ans_find
#     first = find(arr,target,True)
#     last = find(arr,target,False)
#     count = last - first + 1 ## Count formula
#     return count

# print(first_last_occurrences([1,3,3,3,3,3,5,7],3))


## Another way using 2 functions 
def first(arr,target):
    left = 0
    right = len(arr) - 1
    ans = -1 
    while left <= right:
        mid = left + (right-left) // 2
        if arr[mid] == target:
            ans = mid 
            right = mid - 1 
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return ans

def last(arr,target):
    left = 0
    right = len(arr) - 1
    ans = -1 
    while left <= right:
        mid = left + (right-left) // 2
        if arr[mid] == target:
            ans = mid 
            left = mid + 1 
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return ans

arr = [1,3,3,3,3,3,5,7]
target = 3
first = first(arr,target)
last = last(arr,target)
print("Count =",last - first + 1)