def solution(N, number):
    dp = []
    for i in range(1, 9):
        Set = set()
        Set.add(int(str(N)*i))
        for j in range(i-1):
            for ele1 in dp[j]:
                for ele2 in dp[len(dp)-j-1]:
                    Set.add(ele1+ele2)
                    Set.add(ele1-ele2)
                    Set.add(ele1*ele2)
                    if ele2!=0:
                        Set.add(ele1//ele2)
        if number in Set:
            return i
        dp.append(Set)
    return -1