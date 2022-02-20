n, k = map(int, input().split())

result = [[1],[1, 1],[1,2,1]]

for i in range(3, n+1):
  List = [1]
  for j in range(1,i):

    var = result[i-1][j-1]+result[i-1][j]
    List.append(var)
  List.append(1)
  result.append(List)

print(result[n][k]%10007)