c, p = input().split(" ")
c = int(c)
p = int(p)

lucro = 0
for i in range(3):
    q, l = input().split(" ")
    q = int(q)
    l = int(l)
    if c/q <= c:
        lucro = c/q
    else:
        continue
if lucro == 0:
    print("IMPOSSIVEL")
else:
    print(int(lucro))
