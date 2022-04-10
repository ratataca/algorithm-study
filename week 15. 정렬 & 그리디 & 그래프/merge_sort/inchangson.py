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
        print('merged data:', merge_sort_nums)
    
    
    start_selection = time.time()
    selection_sort_nums = selection_sort(origin_nums)
    end_selection = time.time()
    
    if check_sorted(selection_sort_nums) == False:
        print('*' * buf, 'ERROR: NOT SORTED... FUNCTION : selection_sort_nums', '*' * buf)

    if is_print_values:
        print('selection data:', selection_sort_nums)
    
    print(f'성능 비교: merge -> {end_merge - start_merge:.5f}sec || selection -> {end_selection - start_selection:.5f}sec')
    
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

if __name__ == '__main__':
    main()