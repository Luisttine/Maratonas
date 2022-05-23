z = float(input())
a = 23000000000
b = 1000000000000
cont = 0

while b > 0:
    a += a * z / 100 
    b -= a
    cont+=1

print(2016+cont)
