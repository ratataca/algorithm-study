def check_network(cur_node, visited, computers):
    for next_node in range(len(computers)):
        if next_node == cur_node:
            continue
        if not computers[cur_node][next_node]:#check reverse direction too ?
            continue
        if visited[next_node]:
            continue
        visited[next_node] = True
        check_network(next_node, visited, computers)
    return


def solution(n, computers):
    answer = 0
    visited = [False]*n
    for i in range(n):
        if (visited[i]):
            continue
        check_network(i, visited, computers)
        answer += 1
    return answer