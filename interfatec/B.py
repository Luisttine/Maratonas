t = int(input())
cont = 0

for i in range(t):
  cont = 0
  n, m = map(int, input().split(' '))
  arr = list(map(int, input().split(' ')))
  arr.sort()
  for x in arr:
    if x <= m:
      m = m-x
      cont +=1
    else:
      break
  print(cont)
