valor = int(input())

for i in range(valor):
    x, y = map(int, input().split())
    soma = 0

    if x > y:
     for n in range(y+1, x):
        if n %2 != 0:   #esse for é para repetir os que estão entre x e y 
          soma += n
     print(soma) 

  
    else:
       for n in range(x+1, y):
        if n %2 != 0:
          soma += n
       print(soma) 
  
