def sol():
    cnt =int(input())
    nums= list(map(int,input().split()))
    nums.sort()
    ans = nums[0] * nums[-1] 
    return ans

print(sol())