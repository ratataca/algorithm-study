def solution(n, costs):
    def find(parent, n):
        if parent[n] != n:
            parent[n] = find(parent, parent[n])
        return parent[n]

    def union(parent, a, b):
        a = find(parent, a)
        b = find(parent, b)
        if a > b:
            parent[a] = b
        else:
            parent[b] = a

    answer = 0

    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]
    cnt = 0
    for node_a, node_b, cost in costs:
        if cnt == n - 1:
            break
        if find(parent, node_a) != find(parent, node_b):
            union(parent, node_a, node_b)
            answer += cost
            cnt += 1

    return answer
