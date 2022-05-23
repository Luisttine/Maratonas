def sortFn(item):
  return item[1]
n = int(input())
names = {}
order = 0
for i in range(n):
  name = input()
  names[name] = order
  order += 1

data = list(names.items())
data.sort(key=sortFn,reverse=True)
for name in data:
  print(name[0])

