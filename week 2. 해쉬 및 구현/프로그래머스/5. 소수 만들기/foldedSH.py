from itertools import combinations

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

def solution(nums):
    answer = -1

    comb_nums = list(map(sum, combinations(nums, 3)))
    answer = sum([is_prime(i) for i in comb_nums])

    return answer