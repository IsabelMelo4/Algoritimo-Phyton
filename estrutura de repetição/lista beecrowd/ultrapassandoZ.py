cont = 0
somador = 0
x = int(input())

while True:
    z = int(input())
    if z < x:
     continue
    else:
          break

i = x
while somador < z:
    somador += i  
    cont += 1     
    i += 1       
print(cont)