from collections import defaultdict
n = int(input())
m = int(input())

List = defaultdict(list)
for _ in range(m):
  a, b = map(int, input().split())
  List[a].append(b)
  List[b].append(a)

fr = []
fr.extend(List[1])
for i in List[1]:
  fr.extend(List[i])

answer = len(set(fr)) -1
print(answer if answer>=0 else 0)