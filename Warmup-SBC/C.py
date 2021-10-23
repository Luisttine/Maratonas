n = int(input())
tamanho = []
lado = []
x = 0
botas = 0
lados = 0
pares = 0

while x < n:
    m,l = input().split(" ")
    tamanho.append(m)
    lado.append(l)
    x = x+1

i = 0
while i < len(tamanho):
    t = tamanho[i]
    l = lado[i]
    tamanho.sort()
    if t in tamanho[i+1:]:
        botas = botas+1
        tamanho = tamanho[:i]
    else:
        continue
    i = i+1

print(pares/2)
