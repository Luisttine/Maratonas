n = int(input())
x = 0
teste = ''


while x < n:
    out = ''
    l1 = 0
    l2 = 0
    l3 = 0
    teste = input()
    x = x+1

    for i in teste:
        if i == 'A' and l1 == 0:
            out = out+'D'
            l1 = 1
        elif i == 'A' and l1 == 1 and l2 == 0:
            out = out+'D'
            l1 = 0
            l2 = 1
        elif i == 'A' and l1 == 1 and l2 == 1:
            out = out+'E'
            l1 = 0
            l2 = 0

        if i == 'B' and l2 == 0:
            out = out+'D'
            l2 = 1
        elif i == 'B' and l2 == 1:
            out = out+'E'
            l2 = 0
        
        if i == 'C' and l3 == 0 and l2 == 0:
            out = out+'D'
            l3 = 1
            l2 = 1
        elif i == 'C' and l3 == 0 and l2 == 1:
            out = out+'E'
            l3 = 1
            l2 = 0
        elif i == 'C' and l3 == 1:
            out = out+'E'
            l3 = 0
    print(out)




