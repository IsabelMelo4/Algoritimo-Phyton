repeticao = int(input())

for i in range(repeticao):
    n1, n2, ope, d1, d2 = input().split()
    n1 = float(n1)
    n2 = float(n2)
    d1 = float(d1)
    d2 = float(d2)

    if ope == "+":
      print((n1*d2) + (n2*d1))
    elif ope == "-":
      print((n1*d2 - n2*d1) / (d1*d2))
    elif ope == "*":
      print((n1/d2) * (n2/d1))
    elif ope == "/":
      print((n1/d2) / (n2/d1))
    
    