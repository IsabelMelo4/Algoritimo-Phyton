#ler um numero  e digitar ele por extenso 

extenso = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez")

num = int(input("Digite um numero entre o intervalo de 0 a 10"))

while num < 0  or num > 10:
      
      print("tente novamente.")
      num = int(input("Digite um numero entre o intervalo de 0 a 10"))

print("voce escolheu o numero", extenso[num])