n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0]=1

cnt = 0
dp = [[-1 for _ in range(n)] for _ in range(n)]
def recur(x,y):
  global cnt
  if x == n-1 and y == n-1:
    cnt+=1
    return

  if dp[x][y] == -1:  
    dp[x][y] = 0
    if 0<=x+matrix[x][y]<n:
      recur(x+matrix[x][y],y)
    if 0<=y+matrix[x][y]<n:
      recur(x,y+matrix[x][y])

recur(0,0)
print(cnt)

# dp = [[-1 for _ in range(n)] for _ in range(n)]
# def recur(x,y):
#   if x == n-1 and y == n-1:
#     return 1

#   if dp[x][y] == -1:  
#     dp[x][y] = 0
#     if 0<=x+matrix[x][y]<n:
#       dp[x][y]+=recur(x+matrix[x][y],y)
#     if 0<=y+matrix[x][y]<n:
#       dp[x][y]+=recur(x,y+matrix[x][y])

#   return dp[x][y]

# print(recur(0,0))
# print(dp)
