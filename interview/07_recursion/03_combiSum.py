def getPermuts(arr, n, s, idx, csum, cidx, eles, out):
  if csum == s:
    # print('(%s)' % (' '.join(map(str, eles[:cidx]))), end='')
    seq = tuple(eles[:cidx])
    if seq not in out:
      out.append(seq)
  if csum >= s or idx >= n:
    return
  eles[cidx] = arr[idx]
  getPermuts(arr, n, s, idx + 1, csum + arr[idx], cidx + 1, eles, out)
  getPermuts(arr, n, s, idx + 1, csum, cidx, eles, out)


t = int(input())
for i in range(t):
  n = int(input())
  arr = sorted(list(map(int, input().strip().split())))
  s = int(input())
  out = []
  eles = [None] * n
  getPermuts(arr, n, s, 0, 0, 0, eles, out)
  if len(out) == 0:
    print('Empty', end='')
  else:
    print(
        ''.join(
            list(map(lambda x: '(%s)' % (' '.join(list(map(str, x)))), out))),
        end='')
  print()
