n = int(input())

def dec_bin(n):
  return bin(n)

def bin_dec(n):
  return int(n, 2)

for i in range(n):
  a = int(input())

  if a%2 == 1:
    print(a)
  else:
    bin_a = dec_bin(a)
    bin_num = bin_a[2:]
    revert_bin = "0b"+bin_num[::-1]
    print(bin_dec(revert_bin))
    
