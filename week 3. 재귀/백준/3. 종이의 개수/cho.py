from collections import defaultdict
n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]

Dict = defaultdict(int)


def show_matrix(mat):
  for i in matrix:
    for j in i :
      print(j, end=" ")
    print()


def is_same(mat):
  prev = mat[0][0]
  for i in range(len(mat)):
    for j in range(len(mat)):
      if prev != mat[i][j]:
        return False
      else:
        prev = mat[i][j]
  return True

def recursive(mat):
  size = len(mat)
  if is_same(mat):
    Dict[mat[0][0]]+=1
    return


  recursive([row[0:size//3] for row in mat[0:size//3]])
  recursive([row[size//3:(size//3)*2] for row in mat[0:size//3]])
  recursive([row[(size//3)*2:(size//3)*3] for row in mat[0:size//3]])

  recursive([row[0:size//3] for row in mat[(size//3):(size//3)*2]])
  recursive([row[(size//3):(size//3)*2] for row in mat[(size//3):(size//3)*2]])
  recursive([row[(size//3)*2:(size//3)*3] for row in mat[(size//3):(size//3)*2]])

  recursive([row[0:size//3] for row in mat[(size//3)*2:(size//3)*3]])
  recursive([row[(size//3):(size//3)*2] for row in mat[(size//3)*2:(size//3)*3]])
  recursive([row[(size//3)*2:(size//3)*3] for row in mat[(size//3)*2:(size//3)*3]])

recursive(matrix)
print(Dict[-1])
print(Dict[0])
print(Dict[1])