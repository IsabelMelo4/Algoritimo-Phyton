n = int(input())

if n == 1:
    print(0)
elif n == 2:
  print("0 1")

else:
   anterior = 0
   proximo = 1
   print("0 1", end =" ")

   for i in range(n -2):
      
      soma = anterior + proximo
      anterior = proximo
      proximo = soma

      if i == n - 3:
         print(proximo)
      else:
         print(proximo, end=" ") 