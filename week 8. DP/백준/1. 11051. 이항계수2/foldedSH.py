n, k = map(int, input().split())
d = [1]*1001

for i in range(1, n+1):
    d[i] = i*d[i-1]
    
print(int(d[n]//(d[k]*d[n-k]) % 10007))