import math
def solution(nums):
    nums = sorted(nums)
    length = len(nums)
    startPoint = 0
    sumList = []
    answer = 0
    for i in range(startPoint,length - 2):
        for j in range(i+1, length - 1):
            for z in range(j+1, length):
                sumValue = nums[i] + nums[j] + nums[z]
                sumList.append(sumValue)
    def isPrime(x):
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True
     
    for sumValue in sumList:
        if isPrime(sumValue):
            answer +=1


    return answer