reverses = {
  "A":"A",
  "E":"3",
  "H":"H",
  "I":"I",
  "J":"L",
  "L":"J",
  "M":"M",
  "N":"N",
  "O":"O",
  "S":"2",
  "T":"T",
  "U":"U",
  "V":"V",
  "W":"W",
  "X":"X",
  "Y":"Y",
  "Z":"5",
  "1":"1",
  "2":"S",
  "3":"E",
  "5":"z",
  "8":"8"

}

def is_palindrome(s):
  return s == s[::-1]
def is_mirror(s):
  is_true = True
  for i in range((len(s)+1)//2):
    is_true = is_true and s[i] == reverses[s[len(s)-i-1]]
  return is_true

while True:
  try:
    s = input()
    is_p = is_palindrome(s)
    is_m = is_mirror(s)
    if is_p and is_m:
      print(s, "-- is a mirrored palindrome.")
    elif is_p:
      print(s, "-- is a regular palindrome.")
    elif is_m:
      print(s , "-- is a mirrored string.")
    else:
      print(s, " -- is not a palindrome." )
  except EOFError:
    break
