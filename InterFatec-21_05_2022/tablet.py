n = input().split()
m = []
for i in range(0, (int(n[0]))):
    t = input().split()
    if t[2] <= n[1]:
        m.append(int(t[0])*int(t[1]))
if len(m) == 0: print('sem tablet')
else: print(max(m))
