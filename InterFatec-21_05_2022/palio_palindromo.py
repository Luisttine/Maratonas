senhas = int(input())
n = '0123456789'
for i in range(senhas):
    r = ''
    senha = input()
    for l in senha:
        if l in n:
            r += l
    if r == r[::-1]: print('fraca')
    else: print('forte')
