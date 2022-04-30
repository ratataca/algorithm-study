from collections import deque
from random import *
from typing import List
import copy
import time
from xmlrpc.client import boolean

def make_nums():
    nums = list(range(1, randint(1000, 2000)))
    shuffle(nums)
    return nums

def merge(list1: List[int], list2: List[int]) -> List[int]:
    sorted = []
    
    idx1 = 0
    idx2 = 0

    while idx1 < len(list1) and idx2 < len(list2):
        if list1[idx1] < list2[idx2]:
            sorted.append(list1[idx1])
            idx1 += 1
        else:
            sorted.append(list2[idx2])
            idx2 += 1
            
    
    if idx1 < len(list1):
        for i in range(idx1, len(list1)):
            sorted.append(list1[i])
        # sorted += list1[idx1:]
    if idx2 < len(list2):
        for i in range(idx2, len(list2)):
            sorted.append(list2[i])
        # sorted += list2[idx2:]
    
    return sorted

def merge_sort(data: List[int]) -> List[int]:
    leng = len(data)
    if leng <= 1:
        return data
    
    left  = merge_sort(data[:leng//2])
    right = merge_sort(data[leng//2:])
    
    return merge(left, right)


def selection_sort(data: List[int]) -> List[int]:
    sorted = copy.deepcopy(data)
    for i in range(len(sorted) - 1):
        for j in range(i+1, len(sorted)):
            if sorted[i] > sorted[j]:
                sorted[i], sorted[j] = sorted[j], sorted[i]
    return sorted

def quick_sort(data: List[int]) -> List[int]:
    if len(data) <= 1:
        return data
    
    pivot_idx = len(data) // 2
    pivot = data[pivot_idx]

    left  = []
    right = []

    for idx in range(len(data)):
        if idx == pivot_idx:
            continue
        if data[idx] <= pivot:
            left.append(data[idx])
        else:
            right.append(data[idx])
    
    return quick_sort(left) + [pivot] + quick_sort(right)

def check_sorted(data: List[int]) -> boolean:
    pre = data[0]
    for cur in range(1, len(data)):
        if pre > cur:
            return False
    return True

def test(is_print_values: boolean = False):
    origin_nums = make_nums()
    if is_print_values:
        print('origin data:', origin_nums)

    start_merge = time.time()
    merge_sort_nums = merge_sort(origin_nums)
    end_merge = time.time()

    buf = 50
    if check_sorted(merge_sort_nums) == False:
        print('*' * buf, 'ERROR: NOT SORTED... FUNCTION : merge_sort_nums', '*' * buf)

    if is_print_values:
        print('merge sort data:', merge_sort_nums)
    
    
    start_selection = time.time()
    selection_sort_nums = selection_sort(origin_nums)
    end_selection = time.time()
    
    if check_sorted(selection_sort_nums) == False:
        print('*' * buf, 'ERROR: NOT SORTED... FUNCTION : selection_sort_nums', '*' * buf)

    if is_print_values:
        print('selection sort data:', selection_sort_nums)
    
    start_quick = time.time()
    quick_sort_nums = quick_sort(origin_nums)
    end_quick = time.time()

    if check_sorted(quick_sort_nums) == False:
        print('*' * buf, 'ERROR: NOT SORTED... FUNCTION : quick_sort_nums', '*' * buf)

    if is_print_values:
        print('quick sort data:', quick_sort_nums)

    print('<<<<< 성능 비교 >>>>>')
    print(f'merge: {end_merge - start_merge:.5f}sec')
    print(f'selection: {end_selection - start_selection:.5f}sec')
    print(f'quick: {end_quick - start_quick:.5f}sec')
    
    return

def main():
    # data input
    t = int(input('테스트 횟수 입력: '))

    # test
    while t:
        buf = 30
        print('='*buf, t, '='*buf)
        test()
        t -= 1
        print('='*(2*buf + len(str(t)) +2), '\n')
    return

def func1(list1):

    for idx in range(len(list1)):
        list1[idx] += idx

    return

def func2(list1, list2, list3, list4, list5, list6, list7, list8, list9, list10):

    for idx in range(len(list1)):
        list1[idx] += idx
        list2[idx] += idx
        list3[idx] += idx
        list4[idx] += idx
        list5[idx] += idx
        list6[idx] += idx
        list7[idx] += idx
        list8[idx] += idx
        list9[idx] += idx
        list10[idx] += idx

    return


def main2():
    n = 500000
    test_arr = list(range(10*n))

    test_arr1 = list(range(n))
    test_arr11 = list(range(n))
    test_arr2 = list(range(n))
    test_arr12 = list(range(n))
    test_arr3 = list(range(n))
    test_arr13 = list(range(n))
    test_arr4 = list(range(n))
    test_arr14 = list(range(n))
    test_arr5 = list(range(n))
    test_arr15 = list(range(n))
    test_arr6 = list(range(n))
    test_arr16 = list(range(n))
    test_arr7 = list(range(n))
    test_arr17 = list(range(n))
    test_arr8 = list(range(n))
    test_arr18 = list(range(n))
    test_arr9 = list(range(n))
    test_arr19 = list(range(n))
    test_arr10 = list(range(n))
    test_arr110 = list(range(n))
    
    start1 = time.time()
    func1(test_arr)
    end1 = time.time()
    
    start2 = time.time()
    func2(test_arr1, test_arr2, test_arr3, test_arr4, test_arr5, test_arr6, test_arr7, test_arr8, test_arr9, test_arr10)
    end2 = time.time()

    print(f'time 1: {end1 - start1:.5f}sec')
    print(f'time 2: {end2 - start2:.5f}sec')


if __name__ == '__main__':
    main()
    #main2()