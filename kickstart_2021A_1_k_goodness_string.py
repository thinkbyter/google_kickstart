# Contest: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140
# Problem: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cca3
# Attempts: 1
# Solved: during contest

T = int(input())

for t in range(1, T + 1):
  n, k = map(int, input().split())
  s = input()
  
  score = 0
  for i in range(n // 2):
    if s[i] != s[n - i - 1]:
      score += 1

  print(f'Case #{t}: {abs(score - k)}')