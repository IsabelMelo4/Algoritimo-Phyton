x, y = map(int, input().split()) #ele vai ler dois numeros o tamanho da linha e a quantidade
cont = 0 #contador para controlar a linha 

for i in range(1, y+1): #vai contar de 1 ate y 
       
       print(i, end=" ") #innves de quebrar linha ele coloca um espaço dai ele 
                         #imprime tudo na mesma linha 
       cont += 1 #conntador vai somando 1 
         
       if cont == x: #se caso ele fique do tamanho da linha que é x 
         print(end="\n")  #ele quebra pra proxima linha 
         cont=0 # e zera o contador 
