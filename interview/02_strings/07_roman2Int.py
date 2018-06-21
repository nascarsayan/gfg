def roman2Int(roman):
  r2i = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
  integer = r2i[roman[-1]]
  for idx in range(len(roman) - 2, -1, -1):
    if r2i[roman[idx]] < r2i[roman[idx + 1]]:
      integer -= r2i[roman[idx]]
    else:
      integer += r2i[roman[idx]]
  return integer


t = int(input())
for et in range(t):
  roman = input().strip().upper()
  print(roman2Int(roman))
