alphabet = "abcdefghijklmnopqrstuvwxyz"
x = int(input())
for i in range(x):
    cont = 0
    contn = 0
    str = input()
    for char in alphabet: 
        if char  in str.lower(): 
            cont+=1
    if cont == 26:
        print("SIM!")
    elif cont >= 20 and cont < 26:
        print("quase")
    else:
        print("nao")
