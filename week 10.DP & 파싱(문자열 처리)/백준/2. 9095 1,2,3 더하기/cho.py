times = int(input())


List = [1, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(3, 11):
    List[i] = List[i - 3] + List[i - 2] + List[i - 1]

for i in range(times):
    n = int(input())
    print(List[n - 1])
