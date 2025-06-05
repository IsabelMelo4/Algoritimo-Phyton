
x = int(input())
z = int(input())

while z < x:
    z = int(input())
    
cont = 1
somador = x

while somador < z:
     x += 1
     somador +=x
     cont += 1
print(cont)