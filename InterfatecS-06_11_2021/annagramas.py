n = int(input())
x = 0
cont = 0


while x < n:
    s1 = input()
    s2 = input()
    x = x+1
    z = 0
    ss2 = sorted(s2)
    
    if len(s1) < len(s2):
        print('ERRO')
        continue
    while len(s2) <= len(s1):
        sub = s1[:len(s2)]
        if sorted(sub) == ss2:
            z = z+1
        s1 = s1[1:]

        
    print(z)
