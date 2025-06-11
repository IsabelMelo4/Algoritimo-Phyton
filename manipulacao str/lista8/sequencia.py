nome = str(input())
nova_palavra = " "

for i in range(len(nome)):
          
          letra = nome[i]
           
          if len(nome[i+1]) == nome.islower() :
             
             letra = nome[i].upper()
             nova_palavra += letra


          else:
            nova_palavra += letra

print(letra)