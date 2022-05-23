n = int(input())
c = input().split()
c = [int(i) for i in c]
c.sort()
a = [c[i] for i in range(n//2)]
b = [c[i] for i in range(n//2, n)]
p = 0
for i in range(len(a)):
    p += int(b[i]) - int(a[i])
print(p)
