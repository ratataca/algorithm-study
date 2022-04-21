def quick_sort(arr) :
    # 리스트 길이 = 1: 정렬 필요 X
    if len(arr) <= 1 :
        return arr

    pivot = arr[0] # 피봇 설정
    left = [] # 피봇 기준으로 작은 수
    right = [] # 피봇 기준으로 큰 수
    for num in arr[1:]:
        if num < pivot :
            left.append(num)
        else:
            right.append(num)
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([7, 4, 5, 2, 6, 8, 9 ,1, 3]))