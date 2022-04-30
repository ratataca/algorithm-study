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

def bubble_sort(data: List[int]) -> List[int]:
    sorted = copy.deepcopy(data)
    for i in range(len(sorted) - 1):
        for j in range(len(sorted) - 1 - i):
            if sorted[j] > sorted[j+1]:
                sorted[j], sorted[j+1] = sorted[j+1], sorted[j]
    return sorted

def insertion_sort(data: List[int]) -> List[int]:
    sorted = copy.deepcopy(data)
    for i in range(1, len(sorted)):
        for j in range(i, 1, -1):
            if sorted[j] > sorted[j - 1]:
                break
            sorted[j], sorted[j - 1] = sorted[j - 1], sorted[j]
    return sorted

def check_sorted(data: List[int]) -> boolean:
    pre = data[0]
    for cur in range(1, len(data)):
        if pre > cur:
            return False
    return True

def test_sorting_func(sorting_func, orgin_nums: List[int], is_print_values: boolean = False):
    start_time = time.time()
    sorted_nums = sorting_func(orgin_nums)
    end_time = time.time()

    buf = 50
    if check_sorted(sorted_nums) == False:
        print('*' * buf, f'ERROR: NOT SORTED... FUNCTION : {sorting_func.__name__}', '*' * buf)

    if is_print_values:
        print('%sed data:'%(sorting_func.__name__), sorted_nums)
    
    return end_time - start_time

def test(is_print_values: boolean = False):
    # make nums
    origin_nums = make_nums()
    if is_print_values:
        print('origin data:', origin_nums)

    test_functions = [selection_sort, bubble_sort, insertion_sort, merge_sort, quick_sort]
    
    result = []
    for test_function in test_functions:
        result.append(test_sorting_func(test_function, origin_nums, is_print_values))

    print('<<<<< 성능 비교 >>>>>')
    for idx in range(len(test_functions)):
        print(f'{test_functions[idx].__name__} : {result[idx]:.5f}sec')
    
    return

def main():
    # data input
    T = int(input('테스트 횟수 입력: '))

    # test
    for test_num in range(T):
        buf = 30
        print('='*buf, test_num + 1, '='*buf)
        test()
        print('='*(2*buf + len(str(test_num)) +2), '\n')

    return

if __name__ == '__main__':
    main()