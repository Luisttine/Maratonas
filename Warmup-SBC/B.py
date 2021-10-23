n, l = input().split()
n = int(n)
l = int(l)
disp = []
disp = input().replace(' ','')
x = 1
y = 1
livre = 0
passes = 0
z = ""

while x < l:
    disp = int(disp)
    if str(x) in str(disp):
        x = x+1
    else:
        livre = livre+1
        x = x+1
    z = z+str(x)

while y < n:
    disp = str(disp)
    if str(y) in disp:
        y = y+1
    else:
        disp2 = disp
        disp2 = disp[:y-1]+str(y)+disp[y:]
        passes = passes+1
        y = y+1
        if str(z) in disp:
            passes = passes+1
            break


print(passes)

