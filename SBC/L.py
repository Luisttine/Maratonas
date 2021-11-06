n, m = input().split()
password = input()
x = 0

while x < int(m):
    l, r = input().split()
    x=x+1
unk = password[(int(l)-int(r))-1:-1]

print(unk)
