n = int(input())

matrix =[['*']*n for _ in range(n)]

def show_matrix(matrix):
  for i in matrix:
    print(''.join(i))

def hole(n, x, y):
  if n == 1:
    return
  else:
    hole(n//3, x, y)
    hole(n//3, x+n//3, y)
    hole(n//3, x+2*n//3, y)
    hole(n//3, x, y+n//3)
    for i in range(n//3):
      for j in range(n//3):
        matrix[x+n//3+i][y+n//3+j]= ' '
    hole(n//3, x+2*n//3, y+n//3)
    hole(n//3, x, y+2*n//3)
    hole(n//3, x+n//3, y+2*n//3)
    hole(n//3, x+2*n//3, y+2*n//3)

hole(n,0,0)
show_matrix(matrix)
