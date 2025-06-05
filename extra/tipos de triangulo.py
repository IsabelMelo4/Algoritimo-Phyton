a, b, c = map(float, input().split())

if (b + c) > a:
     print("NAO FORMA TRIANGULO")

else:  
    if a ** 2 == b**2 + c **2:
     print("TRIANGULO RETANGULO")

    if  b**2 + c **2 > a ** 2 :
     print("TRIANGULO OBTUSANGULO")

    if  b**2 + c **2 < a **2:
     print("TRIANGULO ACUTANGULO")

    if a == b and b == c:
     print("TRIANGULO EQUILATERO")
    
    if a != b or b != c or c != a:
     print("TRIANGULO ISOSCELES ")
