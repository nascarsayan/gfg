def fillGlass(dpG, k, pos):
  i = 0
  dpG[i][i // 2] = k
  while i < pos[0] and dpG[i][i // 2] > 1:
    dpG[i + 1][0] = max((dpG[i][0] - 1) / 2, 0)
    for idx in range(1, i // 2 + 1):
      dpG[i + 1][idx] = max((dpG[i][idx - 1] - 1) / 2, 0) + max(
          (dpG[i][idx] - 1) / 2, 0)
    if i % 2 == 1:
      dpG[i + 1][(i + 1) // 2] = max(dpG[i][i // 2] - 1, 0)
    for idx in range((i // 2) + 1):
      dpG[i][idx] = min(1, dpG[i][idx])
    i += 1
  if pos[1] > pos[0] // 2:
    pos = (pos[0], pos[0] - pos[1])
  # print('\n'.join(list(map(str, dpG))))
  return min(dpG[pos[0]][pos[1]], 1)


t = int(input())
for i in range(t):
  k = int(input())
  i = int(input())
  j = int(input())
  dpG = [[0] * ((c + 1) // 2) for c in range(1, k + 1)]
  print('{0:.6f}'.format(fillGlass(dpG, k, (i - 1, j - 1))))
