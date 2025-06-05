while True:
  y = int(input())

  if y != 0:                #vai verificar se o numero é diferente de zero, se nao ele entra no for
      for i in range(1,y+1):
        if i != y:          #enquando ele nao for o y, ele vai escrever na mesma linha com o espaço
          print(i, end=" ")
        else:               #se for igual o y, ele escreve o numero sem espaço no final
           print(i)
  else:
      break                 #quando for 0 ele para o while 
     