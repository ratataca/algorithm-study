
def count_coins(target, sums):
    if sums == target:
        return 1
    elif sums > target:
        return 0

    result = 0 
    for coin in coins:
        result += count_coins(target, sums + coin)
    
    return result


# N, K = [int(n) for n in input().split()]
# coins = [int(input()) for _ in range(N)]


##test
N, K = 3, 10
coins = [1, 2, 5]

print(count_coins(K, 0))