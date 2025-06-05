
x = int(input())

while x != 0:
    soma = 0
    for i in range(x, x+10):
        if i %2 == 0:
            soma += i 
    print(soma)
    x = int(input())
    

