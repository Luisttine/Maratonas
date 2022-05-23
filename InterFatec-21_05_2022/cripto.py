ch = int(input())
s = input()
alf = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
alf = [' '] + alf
r = ''
for l in s:
    for n in range(len(alf)):
        if alf[n] == l: m = n
    c =(m+ch)%27
    r += alf[c]
print(r)
