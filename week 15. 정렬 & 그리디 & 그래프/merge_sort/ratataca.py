def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = len(list) // 2

    leftList = list[:mid]
    rightList = list[mid:]

    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)

    return merge(leftList, rightList)

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]

        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]

        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
            
    return result


arr = [7, 3, 5, 7, 81, 0, 63, 4] 
print(merge_sort(arr))
