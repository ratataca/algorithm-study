s = input()

def is_right(x):
  length = len(x)
  count = 0
  while True:
    x = x.replace('[]','')
    x = x.replace('()','')
    count+=1
    if x=='':
      return True
    if count>=length//2+1:
      return False

stack = []
if is_right(s):
  for i in range(len(s)):
    if s[i] =='(':
      stack.append('(')
    elif s[i] == '[':
      stack.append('[')

    elif s[i] == ')':
      if stack[-1]== '(':
        stack.pop()
        stack.append(2)
      else:
        total = 0
        for j in range(len(stack)-1,-1,-1):
          if stack[j] == '(':
            total *=2
            stack.pop()
            stack.append(total)
            break
          else:
            total += stack[j]
            stack.pop()

    else :
      if stack[-1]== '[':
        stack[-1] = 3
      else:
        total = 0
        for j in range(len(stack)-1,-1,-1):
          if stack[j] == '[':
            total *=3
            stack.pop()
            stack.append(total)
            break
          else:
            total += stack[j]
            stack.pop()
  print(sum(stack))
else:
  print(0)