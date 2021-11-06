N, K = input().split()
z = 1
num = ''
cor = ''
lista = ''
nnum = ''
ccor = ''

while z < int(N)+1:
    n, c = input().split()
    num = num+str(z)
    cor = cor+c
    z = z+1
    nnum = nnum+n
    ccor = ccor+c

nnumord = sorted(nnum)
ccord = sorted(ccor)


if str(nnumord) in num and str(ccord) in cor:
    print('Y')
else:
    print('fuck')


