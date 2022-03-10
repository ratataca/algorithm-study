n1, n2 = map(int, input().split())
g1 = list(input())
g2 = list(input())
t = int(input())

team = [0]*len(g1)+[1]*len(g2)
move, result = g1[::-1]+g2, g2+g1[::-1]

cnt = 0
base = g1[0]
while t != cnt:
    for i in range(len(move)):
        flag = False
        if (team[i], team[i+1]) == (0, 1):
            team[i], team[i+1] = team[i+1], team[i]
            move[i], move[i+1] = move[i+1], move[i]
            flag = True
            #print(move)
        if i+1 == len(move)-1 or (move[i+1] == base and flag):
            break
    #print()
    cnt +=1    
    if move == result:
        break

print(''.join(move))