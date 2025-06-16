teste = int(input())

for n in range(teste):
    linha = input()

    frase = linha.split() # a frase recebe a linha digitada separadda em frases
    nova_palavra = ""

    for palavra in frase:
      
      nova_palavra += palavra[0] #a nova palavra vai pegar os caracteres na casa 0 de cada palavra da lista frase

    print(nova_palavra)