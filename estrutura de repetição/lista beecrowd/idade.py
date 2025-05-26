contador = 0
somador = 0
idade = int(input())

while idade > 0:
  somador += idade
  contador += 1
  idade = int(input())

media = somador / contador

print(media)