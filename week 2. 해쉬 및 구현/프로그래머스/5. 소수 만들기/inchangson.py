def setIsPrime(isPrime):
    isPrime[0] = isPrime[1] = False
    for p in range(2, int(MX_SZ**0.5 + 1)):
        if isPrime[p]:
            for n in range(p+p, MX_SZ, p):
                isPrime[n] = False
            

def solution(nums):
    answer = 0
    global MX_SZ
    MX_SZ = 3001
    isPrime = [True] * MX_SZ
    setIsPrime(isPrime)
    
    
    leng = len(nums)
    for i in range(leng - 2):
        for j in range(i + 1, leng - 1):
            for k in range(j + 1, leng):
                if isPrime[nums[i] + nums[j] + nums[k]]:
                    answer += 1
        

    return answer