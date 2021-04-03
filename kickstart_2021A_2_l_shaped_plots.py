# Contest: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140
# Problem: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c509
# Attempts: 1
# Solved: during contest
# Remark: passed 1st test set for 8 points, but got TLE on 2nd test set

T = int(input())

def good(r, c):
  count = 0
  for i in range(2, r + 1):
    if c >= i * 2:
      count += 1
    else:
      break
  for j in range(2, c + 1):
    if r >= j * 2:
      count += 1
    else:
      break

  return count

for t in range(1, T + 1):
  R, C = map(int, input().split())
  g = []
  for _ in range(R):
    g.append(list(map(int, input().split())))

  res = 0
  for r in range(R):
    for c in range(C):
      if g[r][c] == 1:
        left = c - 1
        while left >= 0 and g[r][left] == 1:
          left -= 1
          
        right = c + 1
        while right < C and g[r][right] == 1:
          right += 1
          
        up = r - 1
        while up >= 0 and g[up][c] == 1:
          up -= 1
          
        down = r + 1
        while down < R and g[down][c] == 1:
          down += 1
          
        res += count_l(c - left, r - up)
        res += count_l(c - left, down - r)
        res += count_l(right - c, r - up)
        res += count_l(right - c, down - r)
  
  print(f'Case #{t}: {res}')