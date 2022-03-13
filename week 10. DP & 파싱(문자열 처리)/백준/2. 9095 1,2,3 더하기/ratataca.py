def make_case(target, sums):
    if sums == target:
        return 1
    elif sums > target:
        return 0

    result = 0 
    for num in nums:    
        result += make_case(target, sums + num)
    return result


N = int(input())
cases = [int(input()) for _ in range(N)]

nums = [1, 2, 3]
for case in cases:
    print(make_case(case, 0))



