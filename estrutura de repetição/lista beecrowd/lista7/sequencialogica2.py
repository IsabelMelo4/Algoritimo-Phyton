x, y = map(int, input().split())
cont = 0 
for i in range(1, y+1):
       print(i, end=" ") #innves de quebrar linha ele coloca um espaço dai ele 
                         #imprime tudo na mesma linha 
       cont += 1
       if cont == x:
         print(end="\n")   
         cont=0