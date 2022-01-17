from math import sqrt
from itertools import combinations

def is_prime_num(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    rep = list(combinations(nums, r=3))

    for i in rep:
        if is_prime_num(sum(i)):
            answer += 1

    return answer