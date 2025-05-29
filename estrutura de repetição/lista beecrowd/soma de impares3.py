n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    
    somador = 0
    contador  = 0


    while contador < y:
        if x % 2 != 0:
            somador += x
            contador += 1
        x += 1

    
    print(somador)
