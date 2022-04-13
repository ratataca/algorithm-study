def merge_sort(numbers):
    mid = len(numbers)//2
    if mid == 0:
        return numbers
    
    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])

    return merge(left, right)

def merge(nums1, nums2):
    sort_nums = []
    while True:
        if nums1 == [] or nums2 == []:
            break

        if nums1[0] <= nums2[0]:
            sort_nums.append(nums1.pop(0))
        else:
            sort_nums.append(nums2.pop(0))
    
    if nums1:
        sort_nums.extend(nums1)
    if nums2:
        sort_nums.extend(nums2)

    return sort_nums

print(merge_sort([6, 5, 3, 1, 8, 7, 2, 4])) # [1, 2, 3, 4, 5, 6, 7, 8]