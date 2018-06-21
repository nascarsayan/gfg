def checkBal(inp):
  brStack = []
  braces = ['(', ')', '{', '}', '[', ']']
  for b in inp:
    idx = braces.index(b)
    if idx % 2 == 0:
      brStack.append(idx)
    else:
      if len(brStack) == 0 or brStack[-1] != idx - 1:
        return 'not balanced'
      brStack.pop()
  if len(brStack) != 0:
    return 'not balanced'
  else:
    return 'balanced'


t = int(input())
for et in range(t):
  inp = input()
  print(checkBal(inp))
