def revWords(inp):
  return '.'.join(reversed(inp.split('.')))

t = int(input())
for et in range(t):
  inp = input()
  print(revWords(inp))
